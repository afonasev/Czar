#!/usr/bin/env bash
set -e
pip install -r requirements.txt
isort -c
flake8 backend
pylint backend
py.test --cov=./backend
coveralls
