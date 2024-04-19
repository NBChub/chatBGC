# cli.py

"""Console script for chatbgc."""

import logging
from pathlib import Path

import fire

from .app import start_app
from .train import train_model

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class CLI(object):
    """
    Command-line interface for chatBGC.

    chatBGC is a tool for asking questions about biosynthetic gene clusters in your genome collection via LLMs using Retrieval-Augmented Generation (RAG).

    Attributes:
        None
    """

    def __init__(self):
        """
        The constructor for CLI class.

        Parameters:
            None
        """
        pass

    def run(self, duckdb_path, model="duckdb-nsql"):
        """
        Starts the chatBGC interface using the vanna.ai library.

        The run method is used to start the chatBGC tool. It connects to a DuckDB database using the vanna.ai library and starts a Flask app.

        Parameters:
            duckdb_path (str): The path to the DuckDB database.
            model (str, optional): The model to use. Defaults to 'duckdb-nsql'.

        Returns:
            None
        """
        start_app(duckdb_path, model=model)

    def train(
        self,
        duckdb_path,
        model="duckdb-nsql",
        training_folder=str((Path(__file__).parent / "data").resolve()),
    ):
        """
        Trains the model.

        This method is used to train the model using DDL (*.sql) and documentations (*.md) files in the training folder.

        Parameters:
            duckdb_path (str): The path to the DuckDB database.
            model (str, optional): The model to use. Defaults to 'duckdb-nsql'.
            training_folder (str, optional): The path to the training folder. Defaults to 'data' directory in the current file's parent directory.

        Returns:
            None
        """
        train_model(duckdb_path, model=model, training_folder=training_folder)


def main():
    """
    The main function is used to start the CLI for chatBGC.

    Parameters:
        None

    Returns:
        None
    """
    fire.Fire(CLI)


if __name__ == "__main__":
    main()  # pragma: no cover
