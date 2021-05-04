all: tests

.PHONY: \ 
	all \
    clean \
    install \
    linter \
    mutants \
    run \
    tests

clean:
	rm --recursive $$(find . -name "__pycache__")

install:
	pip install --editable .

linter:
	pylint tablero

mutants: install
	mutmut run --paths-to-mutate tablero

run:
	docker run --detach --publish 500:5000 --rm islasgeci/tablero_api

tests: install
	pytest --cov=tablero --cov-report=term --verbose
