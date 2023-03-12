install:
	poetry install
shell:
	poetry shell
build:
	poetry build
test:
	poetry run pytest
lint:
	poetry run flake8 gendiff
json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
yaml:
	poetry run gendiff  tests/fixtures/file1.yaml tests/fixtures/file2.yaml
coverage:
	poetry run pytest --cov --cov-report xml
