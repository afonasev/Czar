#!/usr/bin/env bash
set -e
isort -rc backend
isort -c
flake8 backend
pylint backend
py.test --cov=./backend
