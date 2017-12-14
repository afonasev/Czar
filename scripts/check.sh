#!/usr/bin/env bash
set -e
echo 'isort'
isort -rc backend
isort -c
echo 'yapf'
yapf -ri backend
echo 'flake8'
flake8 backend
echo 'pylint'
pylint --rcfile=setup.cfg backend
echo 'pytest'
py.test --cov=./backend
