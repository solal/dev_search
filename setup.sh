#!/usr/bin/env bash

STEP_0="👋 Starting installation..."
echo ${STEP_0}

STEP_1="Checking out program's directory..."
echo ${STEP_1}
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

STEP_2="Creating virtual environnement to install dependencies..."
echo ${STEP_2}
python3 -m venv env

STEP_3="Activating virtual environnement to install dependencies..."
echo ${STEP_3}
source env/bin/activate

STEP_4="Installing dependencies in virtual environnement..."
echo ${STEP_4}
pip3 install -r requirements.txt

STEP_5="Successfully installed, dependencies. Deactivating virtual environnement..."
echo ${STEP_5}
deactivate

echo "All done installing, thank you! ✅"