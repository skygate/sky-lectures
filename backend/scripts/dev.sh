#!/bin/sh

chmod +x wait_for_databases.sh
./wait_for_databases.sh
env > /etc/environment
python ./skyLectures/manage.py collectstatic --noinput
python ./skyLectures/manage.py migrate --noinput
python ./skyLectures/manage.py runserver 0.0.0.0:8000