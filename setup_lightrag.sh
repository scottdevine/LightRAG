#!/bin/bash
# Setup script for LightRAG

# Navigate to the LightRAG directory
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install LightRAG in development mode
echo "Installing LightRAG in development mode..."
pip install -e .

# Install required packages for the API server
echo "Installing required packages for the API server..."
pip install fastapi uvicorn

# Install authentication packages
echo "Installing authentication packages..."
pip install PyJWT passlib bcrypt

# Install file handling packages
echo "Installing file handling packages..."
pip install aiofiles python-multipart

# Install additional dependencies that might be needed
echo "Installing additional dependencies..."
pip install networkx matplotlib python-jose[cryptography] websockets

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p inputs rag_storage

# Create a basic config file if it doesn't exist
if [ ! -f "config.ini" ]; then
    echo "Creating basic config.ini file..."
    echo "# This is a simplified configuration file for local development" > config.ini
    echo "# We'll use the default storage options (JsonKVStorage, NanoVectorDBStorage, NetworkXStorage)" >> config.ini
fi

echo "Setup complete! You can now start the LightRAG server with:"
echo "source venv/bin/activate && lightrag-server --working-dir ./rag_storage --input-dir ./inputs --llm-binding ollama --llm-model llama3 --embedding-binding ollama --embedding-model nomic-embed-text"
