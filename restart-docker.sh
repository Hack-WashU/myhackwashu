echo "checking updates..."
pip install -r requirements.txt
echo "checking updates...done"
sleep 5s
echo "migrating db..."
python manage.py makemigrations
python manage.py migrate sessions
python manage.py migrate
echo "migrating db...done"
echo "collecting static..."
python manage.py collectstatic --no-input
echo "collecting static...done"
echo "removing all pyc..."
find . -name \*.pyc -delete
echo "removing all pyc...done"
echo "Deploy completed. The game is on!"

echo "creating superuser..."

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --email "organizer@hackwashu.io" \
        --name "organizer@hackwashu.io" || true
fi
