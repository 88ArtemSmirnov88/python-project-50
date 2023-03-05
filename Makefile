poetry install:
	/Users/artem/.local/bin/poetry install
poetry version:
	/Users/artem/.local/bin/poetry --version
poetry shell:
	/Users/artem/.local/bin/poetry shell
build:
	poetry build

lint:
	poetry run flake8 gendiff
