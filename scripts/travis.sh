#!/usr/bin/env bash -e
echo 'pip install'
pip install -r requirements.txt
echo 'isort'
isort -c
echo 'flake8'
flake8 backend
echo 'pylint'
pylint --rcfile=setup.cfg backend
echo 'pytest'
py.test --cov=./backend
echo 'coveralls'
coveralls
