#!/bin/sh
FOLDER=$1

ECHO "************************"
ECHO "CREATING FASTAPI PROJECT"
ECHO "************************"

cp -r . $FOLDER

cd $FOLDER

pip install --upgrade pip

pip install virtualenv

virtualenv .

source ./bin/activate

pip install -r requirements.txt
pre-commit install --install-hooks

ECHO "************************"
ECHO "PROJECT CREATED AT $FOLDER"
ECHO "************************"
