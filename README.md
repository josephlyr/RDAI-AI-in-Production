# RDAI-AI-in-Production 

# Project: Text Summarisation with FastAPI backend

## Overview

This project implements a text summarisation API using FastAPI and the `facebook/bart-large-cnn` model from Hugging Face’s transformers library. The API enables users to submit text input and receive a concise summary based on configurable parameters for summary length. The application is containerized using Docker. This allows it to run consistently across different environments. Once deployed, the container exposes the API on port 8000, allowing the user to interact via RESTful requests or use the Swagger UI for testing.

## Model

The summarisation model is implemented in `model/model.py`. It uses the **facebook/bart-large-cnn** model from Hugging Face to generate text summaries. The model takes in input text and produces a summary within the specified length range.

### Key Functions:

- `summarise_text(text: str, max_length: int, min_length: int) -> str`: Summarises the given text based on length constraints.
- `main()`: Command-line interface to summarise text.

## Backend Application

The FastAPI backend is defined in `app/main.py`. It exposes an API endpoint to serve summarisation requests.

### Endpoints:

- `GET /` - Returns a welcome message.
- `POST /summarise/` - Accepts text input and returns a summarised version.

### Request Example:

```json
{
    "text": "Long input text that needs summarisation...",
    "max_length": 150,
    "min_length": 50
}
```

### Response Example:

```json
{
    "summary": "Shortened version of the input text."
}
```

## Dockerfile

The application is containerized using Docker, with the setup defined in `Dockerfile`.

### Key Steps:

1. Uses `python:3.12-slim` as the base image.
2. Copies dependencies from `requirements.txt` and installs them.
3. Copies application code into the container.
4. Exposes port `8000` and runs `uvicorn` to serve the FastAPI app.

## Required Packages

Dependencies are listed in `requirements.txt`:

```
fastapi
uvicorn
transformers
torch
pydantic
```

## Running the Containerized Application

The script `run.sh` automates building and running the container.

### Steps to Run:

1. Build the Docker image:
   ```bash
   bash run.sh
   ```
2. The API will be accessible at `http://localhost:8000`.

### Sending a Request

After running the container, you can test the API using `curl`:

```bash
curl -X POST "http://localhost:8000/summarise/" \
     -H "Content-Type: application/json" \
     -d '{"text": "Your long text here", "max_length": 150, "min_length": 50}'
```

Or use the interactive Swagger UI at `http://localhost:8000/docs`.


