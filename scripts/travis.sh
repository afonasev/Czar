#!/usr/bin/env bash -e
pip install -r requirements.txt
isort -c
flake8 backend
pylint --rcfile=setup.cfg backend
py.test --cov=./backend
coveralls
