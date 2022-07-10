#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INTERPRETER_PATH="${SCRIPT_DIR}/env/bin/python3"
SCRIPT_PATH="${SCRIPT_DIR}/devsearch.py"
$INTERPRETER_PATH $SCRIPT_PATH
