#!/usr/bin/env bash -e
isort -rc backend
isort -c
flake8 backend
pylint --rcfile=setup.cfg backend
py.test --cov=./backend
