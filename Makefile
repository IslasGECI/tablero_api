all: check coverage mutants

.PHONY: \
	all \
	check \
	clean \
	coverage \
	format \
	init \
	install \
	linter \
	mutants \
	setup \
	start \
	tests

module = tablero
codecov_token = 8190b206-7a1c-4772-91c5-969521bdc433

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 api.py
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 api.py
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests


clean:
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose

format:
	black --line-length 100 ${module}
	black --line-length 100 api.py
	black --line-length 100 tests

init: setup tests

install:
	pip install --editable .

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${module}
	mutmut run --paths-to-mutate api.py

setup: clean install
	cp data/testmake.header.csv data/testmake.log.csv

start: install
	python -m api

tests:
	pytest --cov=tablero --cov-report=term --verbose
