#!/bin/bash
echo "setting hf token"
if [[ -z "$1" ]]; then
    echo "Token is empty"
    exit 1
fi

# set the HF token
export HUGGING_FACE_HUB_TOKEN=$1

# update the bashrc for persistence
export_command="export HUGGING_FACE_HUB_TOKEN=$1"
echo "$export_command" >> ~/.bashrc

# create a docker.env file
env_file="./docker.env"
# store environment variables required for docker run
echo "HUGGING_FACE_HUB_TOKEN=$1" > $env_file

# messages to user
echo "The Hugging Face token you have set"