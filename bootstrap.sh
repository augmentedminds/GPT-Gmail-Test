#!/bin/sh
export FLASK_APP=./router/router.py
pipenv run flask --debug run -h 0.0.0.0