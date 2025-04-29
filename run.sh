#!/bin/bash

APP_NAME="fmanager"
INSTALL_DIR="/opt/$APP_NAME"

source "$INSTALL_DIR/venv"/bin/activate

python3 "$INSTALL_DIR/main.py" "$@"

deactivate