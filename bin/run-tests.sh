#!/bin/bash

set -exo pipefail

flake8 basket
black --check basket
urlwait
python manage.py makemigrations | grep "No changes detected"
bin/post-deploy.sh
py.test basket \
  --cov-config=.coveragerc \
  --cov-report=html \
  --cov-report=term-missing \
  --cov=.
