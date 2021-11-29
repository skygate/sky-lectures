#!/bin/sh

chmod +x wait_for_databases.sh
./wait_for_databases.sh
env > /etc/environment
python ./skyLectures/manage.py collectstatic --noinput
python ./skyLectures/manage.py migrate --noinput
uwsgi --http :8000 --chdir ./skyLectures --wsgi-file ../skyLectures/skyLectures/wsgi.py
