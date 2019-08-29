all: install tests

.PHONY: build install run tests

build:
	docker build --tag=islasgeci/tablero_api .

install:
	pip install --editable .

run:
	docker run --detach --publish 500:5000 --rm islasgeci/tablero_api

tests:
	pytest --cov=tablero --cov-report=term --verbose
