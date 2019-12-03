mm makemigrations:
	DJANGO_SETTINGS_MODULE=northpole.settings.development python manage.py makemigrations

m migrate:
	DJANGO_SETTINGS_MODULE=northpole.settings.development python manage.py migrate

f fixtures:
	DJANGO_SETTINGS_MODULE=northpole.settings.development python manage.py loaddata northpole/fixtures

s start:
	DJANGO_SETTINGS_MODULE=northpole.settings.development python manage.py runserver

sh shell:
	DJANGO_SETTINGS_MODULE=northpole.settings.development python manage.py shell_plus

t test:
	DJANGO_SETTINGS_MODULE=northpole.settings.testing python manage.py test

# Docker commands
dm dockermigrate:
	DJANGO_SETTINGS_MODULE=northpole.settings.development_docker python3 manage.py migrate

df dockerfixtures:
	DJANGO_SETTINGS_MODULE=northpole.settings.development_docker python3 manage.py loaddata northpole/fixtures

dsh dockershell:
	DJANGO_SETTINGS_MODULE=northpole.settings.development_docker python3 manage.py shell_plus

collectstatic:
	 DJANGO_SETTINGS_MODULE=northpole.settings.development_docker python3 manage.py collectstatic
