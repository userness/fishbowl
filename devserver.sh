#!/bin/sh
. .venv/bin/activate
#python -m flask --app main run --debug
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=${PORT:-5000}
