# AI Markdown Generator

## Description

AI Markdown Generator is a tool that facilitates the conversion of content from various text formats to Markdown format. It uses language models to optimize the generated content and provide more precise editing.

## Features

- Conversion of PDF, PowerPoint, Word, Excel, HTML, CSV, JSON, and XML files to Markdown.
- Optimization of Markdown content using language models.
- Intuitive user interface with Streamlit.
- Support for multiple language model providers (OpenAI, Ollama).

## Dependencies

- `streamlit==1.41.1`
- `markitdown==0.0.1a3`
- `langchain==0.3.14`
- `python-dotenv==1.0.1`
- `langchain-ollama==0.2.2`
- `langchain-openai==0.3.0`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/dominguesleo/ai-markdown-generator.git
    cd ai_markdown_generator
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure the environment variables:
    Create a `.env` file in the root of the project and add the following variables:

    ```env
    PROVIDER=openai  # or 'ollama'
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_MODEL=openai_model_name
    OLLAMA_URL=your_ollama_url
    OLLAMA_MODEL=ollama_model_name
    TEMPERATURE=0.7
    MAX_OUTPUT_TOKENS=1000
    ```

## Environment Variable Configuration

The `.env` file contains the necessary environment variables to configure the application. Below is the usage and meaning of each:

- `PROVIDER`: Specifies the language model provider to use. It can be `openai` or `ollama`.
- `MAX_OUTPUT_TOKENS`: Maximum number of tokens the language model can generate in a single response. **Note:** This variable is not currently in use and is prepared for a future implementation of handling long texts.
- `TEMPERATURE`: Controls the randomness of the model's responses. Lower values make the responses more deterministic.
- `INSTALL_OLLAMA`: Indicates whether Ollama should be installed automatically. It can be `true` or `false`.
- `OLLAMA_URL`: URL of the Ollama server.
- `OLLAMA_MODEL`: Name of the Ollama model to use.
- `OPENAI_API_KEY`: API key to authenticate requests to OpenAI.
- `OPENAI_MODEL`: Name of the OpenAI model to use.

### Default Environment Variables in Dockerfile

The Dockerfile defines some default environment variables that are used when building and running the Docker container. These variables can be overridden when running the container using the `--env-file` option to specify a `.env` file with custom values.

- `PROVIDER=ollama`: Specifies that the default language model provider is Ollama.
- `MAX_OUTPUT_TOKENS=4000`: Sets the maximum number of tokens the language model can generate in a single response. **Note:** This variable is not currently in use and is prepared for a future implementation of handling long texts.
- `TEMPERATURE=0.7`: Controls the randomness of the model's responses. Lower values make the responses more deterministic.
- `INSTALL_OLLAMA=true`: Indicates that Ollama should be installed automatically when building the container.
- `OLLAMA_URL=http://localhost:11434`: URL of the Ollama server.
- `OLLAMA_MODEL=llama3.2:1b`: Name of the Ollama model to use.
- `OPENAI_API_KEY=`: API key to authenticate requests to OpenAI (empty by default).
- `OPENAI_MODEL=`: Name of the OpenAI model to use (empty by default).

The file is prepared to perform an automatic installation of Ollama with the `llama3.2:1b` model. If you have an installation of Ollama on your computer, you can set `INSTALL_OLLAMA=false` in the `.env` file, specifying the URL and the downloaded model to avoid this process.

## Usage

1. Run the application:

    ```sh
    streamlit run __main__.py
    ```

2. Upload a file from the sidebar and wait for it to be processed.

3. View and download the optimized Markdown content.

## Generate Docker Container

To run the application in a Docker container, follow these steps:

1. Build the Docker image:

    ```sh
    docker build -t ai_markdown_generator .
    ```

2. Run the container:

    ```sh
    docker run -p 8501:8501 --env-file .env ai_markdown_generator
    ```

This will start the application at `http://localhost:8501`.

## Functionality of start.sh

The `start.sh` file is responsible for configuring and running the application depending on the language model provider specified in the environment variables.

1. Checks if the provider is Ollama.
2. If `INSTALL_OLLAMA` is set to `true`, it checks if Ollama is installed and, if not, installs it.
3. Starts the Ollama server and downloads the specified model if it is not already downloaded.
4. Finally, starts the Streamlit application.

```bash
#!/bin/bash

# Check if the provider is Ollama
if [ "$PROVIDER" == "ollama" ]; then
    echo "The provider is Ollama."

    // ...existing code...

    fi
fi

# Start Streamlit app
streamlit run __main__.py
```

## Project Structure

    .
    ├── .env
    ├── .gitignore
    ├── .dockerignore
    ├── Dockerfile
    ├── README.md
    ├── __main__.py
    ├── requirements.txt
    ├── src/
    │   ├── integrations/
    │   │   ├── langchain/
    │   │   │   ├── src/integrations/langchain/base_model.py
    │   │   │   ├── src/integrations/langchain/factory_model.py
    │   │   │   ├── src/integrations/langchain/ollama_model.py
    │   │   │   └── src/integrations/langchain/openai_model.py
    │   │   └── src/integrations/markitdown.py
    │   ├── pages/
    │   │   └── src/pages/generator.py
    │   ├── templates/
    │   │   └── src/templates/optimize_markdown_prompt.txt
    │   └── utils/
    │       ├── src/utils/prompt_utils.py
    │       └── src/utils/text_utils.py
    ├── start.sh
    └── tests/
        ├── tests/test_factory_model.py
        └── tests/test_markitdown.py

## Technologies Used

### Streamlit

**Streamlit** is a Python framework that allows you to quickly and easily create interactive web applications. In this project, Streamlit is used to create the user interface that allows users to upload files, process them, and view the generated Markdown content.

Implementation:

- `__main__.py` and `src/pages/generator.py` contain the configuration and pages of the Streamlit application.
- The `st.sidebar.file_uploader` function allows users to upload files from the sidebar.
- The `st.markdown` function is used to display the Markdown content in the interface.

### MarkItDown

**MarkItDown** is a tool that facilitates the conversion of various file formats to Markdown. In this project, it is used to process uploaded files and convert them to Markdown format.

Implementation:

- `src/integrations/markitdown.py` contains the `MarkdownConverter` class, which uses MarkItDown to convert uploaded files.
- The `file_to_markdown` function handles the conversion of files to Markdown.

### LangChain

**LangChain** is a library that facilitates the integration of language models into applications. In this project, it is used to optimize the generated Markdown content.

Implementation:

- `src/integrations/langchain/` contains the implementations of the language models.
- `base_model.py` defines the abstract base class `BaseLangChainModel`.
- `openai_model.py` and `ollama_model.py` contain the specific implementations for OpenAI and Ollama models, respectively.
- `factory_model.py` provides a factory to create instances of language models based on environment variables.

### LangChain-Ollama and LangChain-OpenAI

**LangChain-Ollama** and **LangChain-OpenAI** are extensions of LangChain that provide specific integrations for Ollama and OpenAI models.

Implementation:

- `src/integrations/langchain/ollama_model.py` uses `langchain_ollama` to integrate the Ollama model.
- `src/integrations/langchain/openai_model.py` uses `langchain_openai` to integrate the OpenAI model.

## Future Work

### Text Recognition in Images

Currently, if the file contains images with text, it is likely that the text will not be recognized. A future implementation will be the use of OCR (Optical Character Recognition) to extract text from images and convert it to Markdown.

### Handling Long Texts

The returned Markdown is limited by the maximum number of tokens that the language model can return. If the text is long, it will be interrupted. A future implementation will be to make sequential calls to the language model to read the entire document without losing the previous context and maintain uniform formatting.
