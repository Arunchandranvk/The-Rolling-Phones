#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the Django project directory
cd onlinemobilestore

# Run database migrations
python manage.py migrate