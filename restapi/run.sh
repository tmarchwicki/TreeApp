#!/bin/bash

cd "$(dirname "$0")"
uvicorn main_neo4j:app --reload --port 8000 --host 0.0.0.0
# uvicorn main:app --reload --port 8000 --host 0.0.0.0
