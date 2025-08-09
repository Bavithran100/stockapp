#!/bin/bash
# Build script for Render deployment

set -o errexit

pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply any pending migrations (if using Django ORM)
# python manage.py migrate

echo "Build completed successfully!"
