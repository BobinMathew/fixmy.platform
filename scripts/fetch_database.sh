#!/bin/sh -e
trap "rm -f latest.dump" EXIT INT TERM
rm -f latest.dump
heroku pg:backups:capture -a fixmyplatform-develop
heroku pg:backups:download -a fixmyplatform-develop
docker-compose run --rm app bash -c "pg_restore -c -O -d docker latest.dump; python manage.py anonymizedata --preserve-staff; python manage.py migrate"