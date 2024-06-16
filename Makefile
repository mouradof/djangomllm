PYTHON := python3
PIP := pip
DJANGO_MANAGE := $(PYTHON) manage.py

setup:
	$(PIP) install -r requirements.txt

migrate:
	$(DJANGO_MANAGE) makemigrations
	$(DJANGO_MANAGE) migrate

run:
	docker-compose up --build

test:
	$(DJANGO_MANAGE) test

makemigrations:
	$(DJANGO_MANAGE) makemigrations

createsuperuser:
	$(DJANGO_MANAGE) createsuperuser