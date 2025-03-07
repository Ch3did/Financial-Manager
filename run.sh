#!/bin/bash

# Default values
APP_NAME="Financial-Manager"
INSTALL_DIR="/opt/$APP_NAME"
VENV_DIR="$INSTALL_DIR/venv"
ENTRY_SCRIPT="$INSTALL_DIR/main.py"

source $VENV_DIR/bin/activate 
nohup python3 $ENTRY_SCRIPT > /dev/null 2>&1 &
deactivate