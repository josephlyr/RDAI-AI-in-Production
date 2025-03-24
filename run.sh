#!/bin/bash

# Build the Docker image
docker build -t summarisation-fastapi-app .

# Run the container, mapping port 8000
docker run -p 8000:8000 summarisation-fastapi-app
