#!/bin/bash

# Start updating local system
sudo apt update

# Define constants
APP_NAME="fmanager"
INSTALL_DIR="/opt/$APP_NAME"
PROFILE_FILE="$HOME/.zshrc"

# Clone your library into /opt
echo "Setting up the application in $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"
sudo echo -r ./* "$INSTALL_DIR/enviroment.conf >> .env"
sudo cp "$INSTALL_DIR"
sudo chown -R $USER:$USER "$INSTALL_DIR"

# Create a virtual environment install dependencies
echo "Creating a virtual environment..."
python3 -m venv "$INSTALL_DIR/venv"
echo "Installing python dependencies on venv..."
source "$INSTALL_DIR/venv/bin/activate"
pip3 install -r "$INSTALL_DIR/requirements.txt"

echo "Creating an alias to run the application..."
ALIAS_COMMAND="alias $APP_NAME='$INSTALL_DIR/run.sh'"
if ! grep -q "$ALIAS_COMMAND" "$PROFILE_FILE"; then
    echo "$ALIAS_COMMAND" >> "$PROFILE_FILE"
    echo "Alias added to $PROFILE_FILE. Use '$APP_NAME' to run the application."
else
    echo "Alias already exists in $PROFILE_FILE."
fi

# Reload the shell profile
echo "Reloading shell profile..."
source "$PROFILE_FILE"

# Create Database
fmanager migrate

# Deactivate venv
deactivate