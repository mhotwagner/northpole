#!/bin/sh

echo "Waiting for Postgres to come online..."
sleep 3
echo "Postgres up"

echo "Migrating"
python3 manage.py migrate

if [ "$LOAD_FIXTURES" = "True" ] || [ "$LOAD_FIXTURES" = "true" ] || [ "$LOAD_FIXTURES" = "1" ]
then
    echo "Loading fixtures"
    python3 manage.py loaddata chatty_mason/fixtures
fi

if [ "$COLLECT_STATIC" = "True" ] || [ "$COLLECT_STATIC" = "true" ] || [ "$COLLECT_STATIC" = "1" ]
then
    echo "Preparing static resources"
    python3 manage.py collectstatic --clear --noinput
fi

echo
echo "Environment Variables"
echo "********************"
env
echo "********************"
echo

echo "Starting server"
gunicorn -b 0.0.0.0:8000 northpole.wsgi:application --access-logfile /var/log/northpole-access.log --log-file -
