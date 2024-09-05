install:
	poetry install

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

help-app:
	poetry run gendiff -h

build: check
	poetry build

.PHONY: install test lint selfcheck check build
