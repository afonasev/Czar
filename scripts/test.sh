set -e
isort -c
flake8 backend
pylint backend
py.test --cov=./backend
