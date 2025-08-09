#!/bin/bash
# Build script for Render deployment

set -o errexit

pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply any pending migrations
python manage.py migrate --run-syncdb

echo "Build completed successfully!"
