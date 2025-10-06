# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Optional: install any extra tools you want permanently
RUN pip install pandas sqlite-utils plotly

WORKDIR /workspaces