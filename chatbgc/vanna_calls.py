import logging
import os

import requests
import streamlit as st
from vanna.chromadb import ChromaDB_VectorStore
from vanna.flask import VannaFlaskApp
from vanna.ollama import Ollama
from vanna.openai import OpenAI_Chat

logging.basicConfig(level=logging.DEBUG)


class MyVannaOllama(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


class MyVannaOpenAI(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


@st.cache_resource(ttl=3600)
def setup_vanna(duckdb_path, model="llama3", llm_type="ollama"):
    """
    Starts the Vanna application with the specified configuration.

    Parameters:
    duckdb_path (str): The path to the DuckDB database.
    model (str, optional): The model to use. Defaults to "llama3" for "ollama" and "gpt-4o" for "openai_chat".
    llm_type (str, optional): The type of language model to use. Defaults to "ollama". Other option is "openai_chat".

    Returns:
    None
    """
    if llm_type not in ["ollama", "openai_chat"]:
        raise ValueError(f"Invalid LLM type: {llm_type}")

    config = {"model": model}

    if llm_type == "openai_chat":

        # change default model
        if model == "llama3":
            model = "gpt-4o"
            config["model"] = model

        openai_api_key = os.environ.get("OPENAI_API_KEY")
        if openai_api_key is None:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        config["api_key"] = openai_api_key

        # get available models
        response = requests.get(
            "https://api.openai.com/v1/models",
            headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
        )

        response.raise_for_status()
        available_models = [model["id"] for model in response.json()["data"]]
        if model not in available_models:
            raise ValueError(f"Invalid model. Expected one of: {available_models}")

        logging.info(f"Using {llm_type} model: {model}")

    if llm_type == "ollama":
        vn = MyVannaOllama(config=config)
    elif llm_type == "openai_chat":
        vn = MyVannaOpenAI(config=config)

    vn.connect_to_duckdb(url=duckdb_path)
    return vn


@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached(_vn):
    return _vn.generate_questions()


@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(_vn, question: str):
    return _vn.generate_sql(question=question, allow_llm_to_see_data=True)


@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(_vn, sql: str):
    return _vn.is_sql_valid(sql=sql)


@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(_vn, sql: str):
    return _vn.run_sql(sql=sql)


@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(_vn, question, sql, df):
    return _vn.should_generate_chart(df=df)


@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(_vn, question, sql, df):
    code = _vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code


@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(_vn, code, df):
    return _vn.get_plotly_figure(plotly_code=code, df=df)


@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(_vn, question, sql, df):
    return _vn.generate_followup_questions(question=question, sql=sql, df=df)


@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(_vn, question, df):
    return _vn.generate_summary(question=question, df=df)
