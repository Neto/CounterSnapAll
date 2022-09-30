#!/bin/bash

tmux new -s Control
flask run --host=0.0.0 --port=8080