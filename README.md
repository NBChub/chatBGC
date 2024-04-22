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

## Configuration

Before running chatBGC, you need to configure the language model platform you want to use: `Ollama` or `OpenAI Chat`.

### Ollama

If you're using Ollama, make sure you have it running as described in the Installation section.

### OpenAI Chat

If you're using OpenAI Chat, you need to set up an API key:

1. Sign up for an account on the [OpenAI website](https://www.openai.com/).
2. Navigate to the [API section](https://platform.openai.com/api-keys) and generate a new API key.
3. Set the API key as an environment variable on your system:

    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```

Replace `"your-api-key"` with the API key you generated on the OpenAI website.

## Installation

Follow these steps to install and run chatBGC:

1. **Set up Ollama (Skip this step if you are using `OpenAI Chat`)**

    [Ollama](https://ollama.com/) is the default prerequisite for chatBGC. If you haven't installed it yet, you can do so using Docker:

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

Before running the chatBGC app, run the training using the given database first. You need to only do this once.

```bash
chatbgc train <path_to_duckdb>
```

To start the chatBGC tool, use the following command:

```bash
chatbgc run <path_to_duckdb>
```

## Credits

This package was created with the [ppw](https://zillionare.github.io/python-project-wizard) tool. For more information, please visit the [project page](https://zillionare.github.io/python-project-wizard/).
