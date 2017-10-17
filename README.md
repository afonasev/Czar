# Czar
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Afonasev/Czar/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/Afonasev/Czar.svg?branch=master)](https://travis-ci.org/Afonasev/Czar)
[![Coverage Status](https://coveralls.io/repos/github/Afonasev/Czar/badge.svg?branch=master)](https://coveralls.io/github/Afonasev/Czar?branch=master)

### For development

##### Run development server
    docker-compose up

##### Run only tests
    docker-compose exec web py.test

##### Sort imports, run linters and run tests with coverage report
    docker-compose exec web sh scripts/check.sh

##### Create fake data for development
    docker-compose exec web python manage.py fill_fake_data

### Run production server
    SECRET_KEY=my_key PORT=my_port docker-compose -f docker-compose.prod.yml up

### Git pre-commit hook (don't forget `chmod +x .git/hooks/pre-commit`)
    #!/usr/bin/env bash
    docker-compose exec -T web sh scripts/check.sh

### Code Style
* [PEP8](https://www.python.org/dev/peps/pep-0008/)
