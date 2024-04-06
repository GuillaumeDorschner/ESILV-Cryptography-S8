FROM python:3.8-slim

RUN apt-get update && apt-get install -y tmux

WORKDIR /orchestrator

COPY ./client /orchestrator/client
COPY ./app /orchestrator/app
COPY entrypoint.sh /orchestrator/
RUN chmod +x /orchestrator/entrypoint.sh

COPY requirements.txt /orchestrator/

RUN pip install --no-cache-dir -r requirements.txt
