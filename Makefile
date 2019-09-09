all: install tests

.PHONY: all \
    build \
    clean \
    install \
    lint \
    mutation \
    run \
    tests \


build:
	docker build --tag=islasgeci/tablero_api .

clean:
	sudo rm --recursive $(find . -name "__pycache__")

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
