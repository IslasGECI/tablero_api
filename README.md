# API para el Tablero de la Reproducibilidad

API para el tablero que verifica la reproducibilidad de nuestros reportes mediante `geci-testmake`.

## Entry Points

### GET

- /api/v1/dashboard

### POST

- /api/v1/records

## Configurar la variable `TABLERO_API_SECRET_KEY`
Lo primero que debemos hacer antes de levantar una instalación es verificar que la variable de
entorno `TABLERO_API_SECRET_KEY` está definida en `~/.vault/.secrets` de la manera siguiente:

```shell
export TABLERO_API_SECRET_KEY=<VALOR DEL TOKEN>
```

Si desearamos crear un nuevo token podemos ejecutar secuencialmente los siguientes comandos:

```python
python3
>> import secrets
>> secrets.token_urlsafe(20)
```

obteniendo como resultado un nuevo token para ser utilizado. Ejemplo: `T4wq9JvpEAjXfK8ACpAuEERcL3w`

Esta variable es el token de seguridad para nuestra API y deberá ser solicitada y configurada por
quienes deseen utilizar nuestra API. 

Después de definir la variable en `~/.vault/.secrets`, deberemos ejecutar el siguiente comando para
cargar dicha variable en el sistema:

```shell
source ~/.vault/.secrets
```

Posteriormente se deberá avisar al resto del equipo de cualquier cambio al valor de esta variable
para que el uso de la herramienta `geci-testmake` no se vea afectado.

## Instrucciones para localhost

```shell
docker build --tag islasgeci/tablero_api:latest .
docker run \
    --detach \
    --env="TABLERO_API_SECRET_KEY=${TABLERO_API_SECRET_KEY}" \
    --name tablero_api \
    --publish 500:5000 \
    --rm \
    --volume tablero_api_vol:/workdir/data \
    islasgeci/tablero_api:latest
```

## Instrucciones para el servidor interno

```shell
docker pull islasgeci/tablero_api:latest
docker run \
    --detach \
    --env="TABLERO_API_SECRET_KEY=${TABLERO_API_SECRET_KEY}" \
    --name tablero_api \
    --publish 500:5000 \
    --rm \
    --volume tablero_api_vol:/workdir/data \
    islasgeci/tablero_api:latest
```

## Como probar la API en localhost
Para probar la API, podemos ejecutar el siguiente comando en nuestra terminal:

```shell
curl \
    --header "Authorization: ${TABLERO_API_SECRET_KEY}" \
    --include \
    --request POST "localhost:500/api/v1/records?analista=minombre"
```

---

Con 💖, el equipo de Ciencia de Datos de GECI 😊
