web: gunicorn -b "0.0.0.0:$PORT" -w 3 real_estate.wsgi
release: python manage.py migrate