# chatBGC

<p align="center">
<a href="https://pypi.python.org/pypi/chatbgc">
    <img src="https://img.shields.io/pypi/v/chatbgc.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/NBChub/chatBGC/actions">
    <img src="https://github.com/NBChub/chatBGC/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>

<a href="https://nbchub.github.io/chatBGC/">
    <img src="https://img.shields.io/website/https/nbchub.github.io/chatBGC/index.html.svg?label=docs&down_message=unavailable&up_message=available" alt="Documentation Status">
</a>

</p>

Ask questions about biosynthetic gene clusters in your genome dataset via LLMs using Retrieval-Augmented Generation.

* Free software: MIT
* Documentation: <https://nbchub.github.io/chatBGC/>
## Installation

Follow these steps to install and run chatBGC:

1. **Set up Ollama**

    [Ollama](https://ollama.com/) is a prerequisite for chatBGC. If you haven't installed it yet, you can do so using Docker:

    ```bash
    docker stop ollama
    docker rm ollama
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    docker exec -it ollama ollama run duckdb-nsql
    ```

2. **Clone and install chatBGC**

    Clone the chatBGC repository, navigate to the repository directory, and install the package using pip:

    ```bash
    git clone https://github.com/NBChub/chatBGC.git
    cd chatBGC
    pip install -e .
    ```

## Features

* Command-line interface for asking questions about biosynthetic gene clusters in your genome collection via LLMs using Retrieval-Augmented Generation (RAG).
* Connects to a DuckDB database using the vanna.ai library and starts a Flask app.

## Usage

To start the chatBGC tool, use the following command:

```bash
chatbgc run --duckdb_path <path_to_duckdb> --model <model>
```

## Credits

This package was created with the [ppw](https://zillionare.github.io/python-project-wizard) tool. For more information, please visit the [project page](https://zillionare.github.io/python-project-wizard/).
