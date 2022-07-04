#!/bin/sh

echo "checking updates..."
./env/bin/pip install -r requirements.txt
echo "checking updates...done"
sleep 5s
echo "migrating db..."
./env/bin/python manage.py makemigrations
./env/bin/python manage.py migrate sessions
./env/bin/python manage.py migrate
echo "migrating db...done"
echo "collecting static..."
./env/bin/python manage.py collectstatic --no-input
echo "collecting static...done"
echo "removing all pyc..."
find . -name \*.pyc -delete
echo "removing all pyc...done"
echo "Deploy completed. The game is on!"

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    ./env/bin/python manage.py createsuperuser \
        --noinput \
        --name $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_USERNAME \
        --password $DJANGO_SUPERUSER_PASSWORD
fi
