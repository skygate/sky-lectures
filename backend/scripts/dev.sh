#!/bin/sh

chmod +x wait_for_databases.sh
./wait_for_databases.sh
env > /etc/environment
python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000