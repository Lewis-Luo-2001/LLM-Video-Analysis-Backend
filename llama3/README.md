# Ollama

## Setup
```bash
// start ollama service
ollama serve

// activate the conda environment
conda activate llama3

// start the llama3 server
uvicorn main:app --reload --host 0.0.0.0 --port 30010

// or run the server in background
nohup uvicorn main:app --host 0.0.0.0 --port 30010 &
// stop the server
pkill uvicorn
```