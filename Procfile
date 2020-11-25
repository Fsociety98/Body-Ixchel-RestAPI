release: python manage.py makemigrations 
release: python manage.py migrate 

web: gunicorn BodyIxchel_Project.wsgi:application --log-file -