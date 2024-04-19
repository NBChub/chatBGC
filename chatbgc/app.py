"""Main module."""

from vanna.chromadb import ChromaDB_VectorStore
from vanna.flask import VannaFlaskApp
from vanna.ollama import Ollama


class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


def start_app(duckdb_path, model="duckdb-nsql"):
    """
    Starts the Vanna application with the specified configuration.

    Parameters:
    duckdb_path (str): The path to the DuckDB database.
    model (str, optional): The model to use. Defaults to "duckdb-nsql".

    Returns:
    None
    """
    vn = MyVanna(config={"model": model})

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
