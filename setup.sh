#!/bin/bash

# Get path of this script and cli_ai.sh script
THIS_DIR=$(cd $(dirname $0); pwd)
SCRIPT_PATH=$THIS_DIR/app/cli_ai.sh
echo $SCRIPT_PATH

# Install dependencies
sudo apt install python3.8 python-is-python3 -y
pip install -r requirements.txt

# Create symlink to cli_ai.sh script
mkdir -p $HOME/.local/bin
ln -s $SCRIPT_PATH $HOME/.local/bin/cli_ai
chmod +x $HOME/.local/bin/cli_ai

# Add symlink directory and CLI_AI_DIR variable to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> $HOME/.bashrc
echo "export CLI_AI_DIR=$THIS_DIR/app" >> $HOME/.bashrc
source $HOME/.bashrc
