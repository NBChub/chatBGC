"""Main module."""

import logging
import os

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


def start_app(duckdb_path, model="duckdb-nsql", llm_type="ollama"):
    """
    Starts the Vanna application with the specified configuration.

    Parameters:
    duckdb_path (str): The path to the DuckDB database.
    model (str, optional): The model to use. Defaults to "duckdb-nsql" for "ollama" and "gpt-4" for "openai_chat".
    llm_type (str, optional): The type of language model to use. Defaults to "ollama". Other option is "openai_chat".

    Returns:
    None
    """
    if llm_type not in ["ollama", "openai_chat"]:
        raise ValueError(f"Invalid LLM type: {llm_type}")

    config = {"model": model}

    if llm_type == "openai_chat":
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        if openai_api_key is None:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        config["api_key"] = openai_api_key
        if model == "duckdb-nsql":
            model = "gpt-4"
            config["model"] = model
        logging.info(f"Using {llm_type} model: {model}")

    if llm_type == "ollama":
        vn = MyVannaOllama(config=config)
    elif llm_type == "openai_chat":
        vn = MyVannaOpenAI(config=config)

    vn.connect_to_duckdb(url=duckdb_path)

    app = VannaFlaskApp(
        vn,
        logo="https://raw.githubusercontent.com/NBChub/chatBGC/dev-0.1.0/chatbgc/assets/bgcflow_logo.png?token=GHSAT0AAAAAACGXSVJOGS4A3BOZBYMHV5FGZRCB6UQ",
        title="Welcome to chatBGC",
        subtitle="Your AI-powered copilot for querying smBGCs in your genome collection.",
        show_training_data=False,
        suggested_questions=False,
        sql=True,
        table=True,
        csv_download=False,
        chart=True,
        redraw_chart=False,
        auto_fix_sql=True,
        ask_results_correct=False,
        followup_questions=True,
        summarization=False,
    )
    app.run()
