# API para el Tablero de Reproducibilidad

API para el tablero de reproducibilidad de nuestros reportes mediante `geci-testmake`.

## Entry Points

### GET

- /api/v1/dashboard

### POST

- /api/v1/records

# Configurar la variable __$TABLERO_API_SECRET_KEY__
Lo primero que debemos hacer antes de levantar una instalación es verificar que la siguiente
variable de entorno en el __~/.vault/.secrets__ está disponible:

```shell
export TABLERO_API_SECRET_KEY=<VALOR DEL TOKEN>
```
Si desearamos crear un nuevo token podemos ejecutar secuencialmente los siguientes comandos:
```python
python3
>> import secrets
>> secrets.token_urlsafe(20)
```
obteniendo como resultado un nuevo token para ser utilizado
Ejemplo: `T4wq9JvpEAjXfK8ACpAuEERcL3w`

Esta variable es el token de seguridad para nuestra API, sera la llave y debera ser solicidata y configurada por quienes deseen utilizar nuestra API. De no tenerla configurada, deberemos solicitar el _token_ al encargado actual del
repositorio y agregarla a nuestro archivo __~/.vault/.secrets__.

Después de configurar la variable, deberemos ejecutar el siguiente comando para cargar dicha variable en el sistema:

```shell
source ~/.vault/.secrets
```


## Instrucciones para localhost

```
docker build --tag islasgeci/tablero_api:latest .
docker run --detach --publish  500:5000 --rm --env="TABLERO_API_SECRET_KEY=${TABLERO_API_SECRET_KEY}" --volume tablero_api_vol:/workdir/data islasgeci/tablero_api:latest
```

## Instrucciones para el servidor interno

```
docker pull islasgeci/tablero_api:latest
docker run --detach --publish  500:5000 --rm --env="TABLERO_API_SECRET_KEY=${TABLERO_API_SECRET_KEY}" --volume tablero_api_vol:/workdir/data islasgeci/tablero_api:latest
```



---

Con 💖, el equipo de Ciencia de Datos de GECI 😊
