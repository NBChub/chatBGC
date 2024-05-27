# cli.py

"""Console script for chatbgc."""

import logging
import sys
from pathlib import Path

import fire

from .app import start_app
from .train import train_model

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
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

    def run(self, duckdb_path, model="llama3", llm_type="ollama"):
        """
        Starts the chatBGC interface using the vanna.ai library.

        The run method is used to start the chatBGC tool. It connects to a DuckDB database using the vanna.ai library and starts a Flask app.

        Parameters:
            duckdb_path (str): The path to the DuckDB database.
            model (str, optional): The model to use. Defaults to "llama3" for "ollama" and "gpt-4o" for "openai_chat".
            llm_type (str, optional): The type of language model to use. Defaults to "ollama". Other option is "openai_chat".

        Returns:
            None
        """
        start_app(duckdb_path, model=model, llm_type=llm_type)

    def train(
        self,
        duckdb_path,
        model="llama3",
        training_folder=str((Path(__file__).parent / "data").resolve()),
        llm_type="ollama",
    ):
        """
        Trains the model.

        This method is used to train the model using DDL (*.sql) and documentations (*.md) files in the training folder.

        Parameters:
            duckdb_path (str): The path to the DuckDB database.
            model (str, optional): The model to use. Defaults to 'llama3'.
            training_folder (str, optional): The path to the training folder. Defaults to 'data' directory in the current file's parent directory.
            llm_type (str, optional): The type of language model to use. Defaults to "ollama". Other option is "openai_chat".

        Returns:
            None
        """
        train_model(
            duckdb_path, model=model, training_folder=training_folder, llm_type=llm_type
        )


def main():
    """
    The main function is used to start the CLI for chatBGC.

    Parameters:
        None

    Returns:
        None
    """
    # Custom helper message
    if len(sys.argv) == 2 and ("-h" in sys.argv or "--help" in sys.argv):
        sys.argv.remove("-h") if "-h" in sys.argv else sys.argv.remove("--help")

    fire.Fire(CLI)


if __name__ == "__main__":
    main()  # pragma: no cover
