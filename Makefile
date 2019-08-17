.PHONY: build run

build:
	docker build --tag=islasgeci/tablero_api .

run:
	docker run --detach --publish 500:5000 --rm islasgeci/tablero_api

