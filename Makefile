
SHELL := /bin/bash

install:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	source venv/bin/activate && python3 project/manage.py runserver
