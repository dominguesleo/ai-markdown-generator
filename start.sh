#!/bin/bash

# Check if the provider is Ollama
if [ "$PROVIDER" == "ollama" ]; then
    echo "The provider is Ollama."

    # Check if the INSTALL_OLLAMA variable is set to true
    if [ "$INSTALL_OLLAMA" == "true" ]; then
        echo "INSTALL_OLLAMA is true. Checking if Ollama is already installed..."

        # Check if Ollama is already installed (by checking if the 'ollama' command exists)
        if ! command -v ollama &> /dev/null; then
            echo "Ollama not found. Installing Ollama and the default model..."
            apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*
            curl -fsSL https://ollama.com/install.sh | sh
        else
            echo "Ollama is already installed. Skipping installation."
        fi

        # Ensure Ollama server is running
        echo "Starting Ollama server..."
        ollama serve &

        sleep 5

        # Use ollama list to check if the model is already downloaded
        if ! ollama list | grep -q "$OLLAMA_MODEL"; then
            echo "Model $OLLAMA_MODEL not found. Downloading the model..."
            ollama pull $OLLAMA_MODEL
        else
            echo "Model $OLLAMA_MODEL already downloaded. Skipping model download."
        fi
    else
        echo "INSTALL_OLLAMA is not set to true. Skipping installation."
    fi
fi

# Start Streamlit app
streamlit run __main__.py