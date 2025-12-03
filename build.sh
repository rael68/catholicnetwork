#!/bin/bash
# Exit on any error
set -e

# Create virtualenv
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
