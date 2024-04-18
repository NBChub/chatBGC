"""Console script for chatbgc."""

import fire


def help() -> None:
    print("chatbgc")
    print("=" * len("chatbgc"))
    print(
        "Ask questions about biosynthetic gene clusters in your genome collection via LLMs using Retrieval-Augmented Generation (RAG)."
    )


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
