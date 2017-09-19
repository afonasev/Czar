set -e
pip install -r requirements.txt
./scripts/test.sh
coveralls
