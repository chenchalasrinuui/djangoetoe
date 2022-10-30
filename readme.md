1. create django project

2. pipenv install django gunicorn whitenoise djangorestframework django-cors-headers djongo pymongo = "3.12.3"

3. pip freeze > requirements.txt

4. create Procfile

   web: gunicorn deployment.wsgi --log-file -

5. create runtime.txt

   python-3.10.1 

6. In settings.py

  a. DEBUG = False
  b. ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
  c. INSTALLED_APPS = [
    	'whitenoise.runserver_nostatic',
    	'django.contrib.staticfiles',
      'rest_framework',
      'corsheaders'
   	# ...
	] 
  d. MIDDLEWARE = [
 	'django.middleware.security.SecurityMiddleware',
 	'whitenoise.middleware.WhiteNoiseMiddleware',
   'corsheaders.middleware.CorsMiddleware',
 	# ...
	]

   e. optional 
 
      WHITENOISE_USE_FINDERS = True
      STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



Note:


To set Heroku version 

    heroku stack:set heroku-20 -a <heroku appname>

    heroku config:set DISABLE_COLLECTSTATIC=1 -a  <heroku appname>

    heroku ps -a <heroku appname>

    heroku logs -a <heroku appname>

    heroku ps:scale worker=1 -a stepupdjango