# Whisper

## Setup
```bash
// activate the conda environment
conda activate whisper

//start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 30011

// or run the server in background
nohup uvicorn main:app --host 0.0.0.0 --port 30011 &
// stop the server
pkill uvicorn
```