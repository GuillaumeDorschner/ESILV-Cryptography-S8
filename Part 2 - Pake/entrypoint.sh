#!/bin/bash

tmux new-session -d \; \
  split-window -h \; \
  send-keys 'flask run --host=0.0.0.0 --port=80' C-m \; \
  select-pane -L \; \
  send-keys 'python -m client.main' C-m \; \
  attach