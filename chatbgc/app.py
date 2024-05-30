"""Main module."""

import logging
import os

import requests
from vanna.chromadb import ChromaDB_VectorStore
from vanna.flask import VannaFlaskApp
from vanna.ollama import Ollama
from vanna.openai import OpenAI_Chat


class MyVannaOllama(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


class MyVannaOpenAI(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


def start_app(duckdb_path, model="llama3", llm_type="ollama"):
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

    app = VannaFlaskApp(
        vn,
        logo="https://raw.githubusercontent.com/NBChub/chatBGC/main/chatbgc/assets/bgcflow_logo.png",
        title="Welcome to chatBGC",
        subtitle="Your AI-powered copilot for querying smBGCs in from BGCFlow run.",
        show_training_data=False,
        suggested_questions=False,
        sql=True,
        table=True,
        csv_download=True,
        chart=True,
        redraw_chart=False,
        auto_fix_sql=True,
        ask_results_correct=True,
        followup_questions=True,
        summarization=True,
        allow_llm_to_see_data=True,
    )
    app.run()
