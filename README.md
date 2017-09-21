# Czar
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Afonasev/Czar/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/Afonasev/Czar.svg?branch=master)](https://travis-ci.org/Afonasev/Czar)
[![Coverage Status](https://coveralls.io/repos/github/Afonasev/Czar/badge.svg?branch=master)](https://coveralls.io/github/Afonasev/Czar?branch=master)

### Run dev server

###### Install deps

    pip install -r requirements.txt

###### Apply migrations
    python manage.py migrate

###### Run debug server

    python manage.py runserver

### Tests, linters, etc.

###### Run all tests and linters

    ./scripts/test.sh

###### Run tests

    py.test --cov=./backend

###### Run linters

    flake8 backend
    pylint backend
    isort -c

###### Sort imports

    isort -rc backend

###### Generate fake data (groups, commands, calls amd etc.)

    python manage.py fill_fake_data

### Run develop server with docker-compose

    docker-compose up

###### Run tests and linters in container

    docker exec -it czar_web_1 sh ./scripts/test.sh

###### Show server logs

    docker logs -f czar_web_1

### Git pre-commit hook

    #!/bin/bash
    set -e
    isort -c
    flake8 backend
    pylint backend
    py.test --cov=./backend

### Code Style

* [PEP8](https://www.python.org/dev/peps/pep-0008/)
