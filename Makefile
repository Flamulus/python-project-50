install:
	poetry install

lint:
	poetry run flake8 .

test:
	poetry run pytest -s

test-cov:
	poetry run pytest --cov

help-app:
	poetry run gendiff -h

build:
	poetry build
