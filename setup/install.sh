#!/bin/bash

set -e

source $(git rev-parse --show-toplevel)/SOURCEME

cd $PYMOD_PATH
python3 setup.py install

cd $PY_PARSER_PATH
python3 setup.py install
