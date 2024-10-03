#!/bin/bash
apt update
apt install software-properties-common

# Install recent Python version
add-apt-repository ppa:deadsnakes/ppa -y
apt install python3.11 python3-pip python3.11-dev python3.11-distutils -y
PY=$(which python3.11)

# Install required packages
cd /autograder/source
$PY -m pip install --upgrade pip
$PY -m pip install --user -r requirements.txt

# Create a symbolic link high on the path for `python` to invoke 3.11
ln -s /usr/bin/python3.11 /usr/local/sbin/python