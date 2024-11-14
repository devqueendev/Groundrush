#!/bin/bash


echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files (if needed)
echo "Collecting static files..."
#python manage.py collectstatic --noinput


# Start Gunicorn with the WSGI application
echo "Starting Gunicorn server..."
exec gunicorn src.core.wsgi:application --bind 0.0.0.0:"$APP_PORT" --workers 3 --log-level=info

