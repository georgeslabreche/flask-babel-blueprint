#!/bin/sh
source ./venv/bin/activate
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l fr