web: gunicorn deployment.wsgi --log-file - --log-level debug
heroku ps:scale web=1
py manage.py migrate