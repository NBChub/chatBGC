# cli.py

"""Console script for chatbgc."""

import fire

from .app import start_app


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
