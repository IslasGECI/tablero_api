.PHONY: build run

build:
	docker build --tag=tablero .

run:
	docker run --detach --publish 5000:5000 --rm --volume $${HOME}/repositorios/tablero/:/workdir tablero

