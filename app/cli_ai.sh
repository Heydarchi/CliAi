#!/bin/bash

# Check the mode provided in the command
if [ -z "$1" ] || [ "$1" == "chat" ]; then
    # Run CliAi in chat mode
    python "$CLI_AI_DIR/CliAi.py" chat
elif [ "$1" == "one-shot" ]; then
    # Shift the first argument to remove the mode
    shift
    # Check if any message is provided
    if [ -z "$1" ]; then
        echo "Please provide at least one message."
    else
        # Run CliAi in one-shot mode with the provided messages
        python "$CLI_AI_DIR/CliAi.py" one-shot "$@"
    fi
elif [ "$1" == "file" ]; then
    # Check if the file path is provided
    if [ -z "$2" ]; then
        echo "Please provide a file path."
    else
        # Run CliAi in file mode with the provided file path
        python "$CLI_AI_DIR/CliAi.py" file "$@"
    fi
elif [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    # Check if the file path is provided
    python "$CLI_AI_DIR/CliAi.py" -h
elif [ "$1" == "stdin" ]; then
    # Read input from stdin and pass it to CliAi
    input=$(cat -)
    echo "$input" | python "$CLI_AI_DIR/CliAi.py" one-shot
else
    echo "Invalid mode specified. Please use 'chat', 'one-shot', 'file', '--help', '-h', or 'stdin'."
fi
