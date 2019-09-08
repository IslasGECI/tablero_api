all: install tests

.PHONY: all \
    build \
    install \
    lint \
    mutation \
    run \
    tests \


build:
	docker build --tag=islasgeci/tablero_api .

install:
	pip install --editable .

lint:
	pylint tablero

mutation:
	mutmut run --paths-to-mutate tablero

run:
	docker run --detach --publish 500:5000 --rm islasgeci/tablero_api

tests:
	pytest --cov=tablero --cov-report=term --verbose
