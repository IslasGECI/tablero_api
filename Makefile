all: check coverage mutants

.PHONY: \
	all \
	check \
	clean \
	coverage \
	format \
	install \
	linter \
	mutants \
	tests

module = tablero
codecov_token = 8190b206-7a1c-4772-91c5-969521bdc433

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 setup.py
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 setup.py
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests


clean:
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: install
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 setup.py
	black --line-length 100 tests

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

mutants: install
	mutmut run --paths-to-mutate ${module}

tests: install
	pytest --cov=tablero --cov-report=term --verbose
