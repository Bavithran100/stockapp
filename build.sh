#!/bin/bash
# Build script for Render deployment

set -o errexit

echo "Starting build process..."

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

echo "Build completed successfully!"
