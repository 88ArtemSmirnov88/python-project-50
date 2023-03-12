poetry install:
	poetry install
poetry shell:
	poetry shell
build:
	poetry build
test:
	poetry run pytest
lint:
	poetry run flake8 gendiff
