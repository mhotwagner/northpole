#!/bin/sh

echo "****************"
echo "** NORTHPOLE **"
echo "****************"
echo ""
echo "Starting stage server"

echo "Migrating database"
python3 manage.py migrate

#if [ "$LOAD_FIXTURES" = "True" ] || [ "$LOAD_FIXTURES" = "true" ] || [ "$LOAD_FIXTURES" = "1" ]
#then
#    echo "Loading fixtures"
#    python3 manage.py loaddata chatty_mason/fixtures
#fi

if [ "$COLLECT_STATIC" = "False" ] || [ "$COLLECT_STATIC" = "false" ] || [ "$COLLECT_STATIC" = "0" ]
then
    echo "Not collectng resources"
else
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
#gunicorn -b 0.0.0.0:8000 northpole.wsgi:application --access-logfile /var/log/northpole-access.log --log-file -
daphne northpole.asgi:application --bind 0.0.0.0 --port $PORT --access-log /var/log/northpole-access.log -v2
#python3 manage.py runserver 0.0.0.0:8080
