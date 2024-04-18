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

    def run(self, email, sqlite_path="https://vanna.ai/Chinook.sqlite"):
        """
        Starts the chatBGC interface using the vanna.ai library.

        The run method is used to start the chatBGC tool. It connects to a SQLite database using the vanna.ai library and starts a Flask app.

        Parameters:
            email (str): The email to use for retrieving the API key from vanna.ai.
            sqlite_path (str, optional): The URL or path to the SQLite database. Defaults to 'https://vanna.ai/Chinook.sqlite'.

        Returns:
            None
        """
        start_app(email, sqlite_path=sqlite_path)


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
