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
	poetry run gendiff tests/fixtures/file.json tests/fixtures/file2.json
yaml:
	poetry run gendiff  tests/fixtures/file1.yaml tests/fixtures/file2.yaml
json_long:
	poetry run gendiff tests/fixtures/file3.json tests/fixtures/file4.json
yaml_long:
	poetry run gendiff  tests/fixtures/file3.yaml tests/fixtures/file4.yaml
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
