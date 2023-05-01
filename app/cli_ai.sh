#!/bin/bash

# Check if input is coming from a pipe
if [ -p /dev/stdin ]; then
    # Read input from stdin and pass it to CliAi
    input=$(cat -)
    # Combine the input from the pipe with the provided arguments
    messages=("$input" "$@")
else
    messages=("$@")
fi

# Check the mode provided in the command
if [ -z "$1" ] || [ "$1" == "chat" ] || [ "$1" == "chatplus" ] ; then
    # Run CliAi in chat mode
    python "$CLI_AI_DIR/CliAi.py" "$1"
elif [ "$1" == "oneshot" ]; then
    # Shift the first argument to remove the mode
    shift
    # Run CliAi in oneshot mode with the combined messages
    python "$CLI_AI_DIR/CliAi.py" oneshot "${messages[@]}"
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
else
    echo "Invalid mode specified. Please use 'chat', 'chatplus', 'oneshot', 'file', '--help', '-h', or pipe input to 'cli_ai oneshot'."
fi
