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
MN_FUNCTION="mn() { ~/code/pessoal/me/CLI-For-Nubank-API/run.sh \"\$@\"; }"
if ! grep -q "$MN_FUNCTION" "$PROFILE_FILE"; then
    echo "$MN_FUNCTION" >> "$PROFILE_FILE"
    echo "Function added to $PROFILE_FILE. Use 'mn' to run the application."
else
    echo "Function already exists in $PROFILE_FILE."
fi

# Reload the shell profile
echo "Reloading shell profile..."
source "$PROFILE_FILE"

# Create Database
fmanager migrate

# Deactivate venv
deactivate