#!/bin/sh
source ./venv/bin/activate
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d app/translations -l sr
pybabel init -i messages.pot -d app/translations -l sq