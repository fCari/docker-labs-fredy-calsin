# Laboratorio 04 - Seguridad y buenas prácticas

## Datos del alumno

**Nombre:** Fredy Calsin
**Imagen:** fredy-calsin-api:v3
**Puerto:** 8083

## Objetivo

Ejecutar el proceso de la aplicación con un usuario distinto de root, conservando su funcionamiento y las optimizaciones del laboratorio 03.

## Cambios respecto al laboratorio 03

1. `RUN addgroup --system ... && adduser --system ...` crea un usuario de sistema sin privilegios (`appuser`).
2. `COPY --chown=appuser:appgroup main.py .` entrega la propiedad del código al usuario creado.
3. `USER appuser` hace que el proceso principal se inicie con ese usuario.
4. Se conservan `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1`, el orden de capas y `.dockerignore`.

## Procedimiento

### 1. Construcción

```bash
docker build -t fredy-calsin-api:v3 .
```

### 2. Ejecución

```bash
docker run -d --name fredy-calsin-api-v3 \
  -p 8083:8000 fredy-calsin-api:v3
```

### 3. Verificación

```bash
docker exec fredy-calsin-api-v3 id
curl http://localhost:8083/health
```

La salida de `id` debe mostrar un UID distinto de 0 (por ejemplo `uid=100(appuser) gid=101(appgroup)`), mientras que root tiene UID 0.

## Evidencias

### Dockerfile con creación de usuario e instrucción USER

![Dockerfile](evidencias/01-dockerfile.png)

### Salida de `docker exec ... id`

![Comando id](evidencias/02-id.png)

### Endpoint `/health` en el puerto 8083

![Health](evidencias/03-health.png)

## Resultado

El contenedor se ejecuta con el usuario `appuser` (UID distinto de 0) y el endpoint `/health` sigue respondiendo `{"status": "ok"}` en el puerto 8083.

## Conclusiones

Ejecutar como root dentro del contenedor aumenta el impacto de una posible vulnerabilidad. Crear un usuario sin privilegios y usar `USER` es una práctica sencilla que reduce ese riesgo sin afectar el funcionamiento de la aplicación.
