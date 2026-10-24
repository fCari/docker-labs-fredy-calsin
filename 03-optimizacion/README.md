# Laboratorio 03 - Optimización del Dockerfile

## Datos del alumno

**Nombre:** Fredy Calsin
**Imagen:** fredy-calsin-api:v2
**Puerto:** 8082

## Objetivo

Optimizar la construcción de la imagen mediante el orden de las capas, el caché de Docker y la exclusión de archivos innecesarios con `.dockerignore`.

## Cambios respecto al laboratorio 02

1. Se copia `requirements.txt` e instala dependencias **antes** de copiar `main.py`.
2. Se agregan las variables de entorno `PYTHONDONTWRITEBYTECODE=1` y `PYTHONUNBUFFERED=1`.
3. Se crea `.dockerignore` para excluir `.git/`, `.venv/`, `__pycache__/`, `*.pyc`, `.env` y `evidencias/`.

## Procedimiento

### 1. Primera construcción

```bash
docker build --progress=plain -t fredy-calsin-api:v2 .
```

### 2. Modificar solo el mensaje en `main.py` y reconstruir (sin `--no-cache`)

```bash
docker build --progress=plain -t fredy-calsin-api:v2 .
```

En esta reconstrucción los pasos de `FROM`, `ENV`, `WORKDIR`, `COPY requirements.txt` y `RUN pip install` aparecen como **CACHED**; solo se vuelve a ejecutar `COPY main.py`.

### 3. Ejecución y prueba

```bash
docker run -d --name fredy-calsin-api-v2 \
  -p 8082:8000 fredy-calsin-api:v2
curl http://localhost:8082/
```

## Evidencias

### Dockerfile optimizado y `.dockerignore`

![Dockerfile y dockerignore](evidencias/01-dockerfile-dockerignore.png)

### Reconstrucción con pasos CACHED

![Reconstrucción con CACHED](evidencias/02-cached.png)

### API respondiendo en el puerto 8082

![API puerto 8082](evidencias/03-api-8082.png)

## Resultado

La reconstrucción tras cambiar solo `main.py` fue rápida porque Docker reutilizó las capas anteriores, incluida la instalación de dependencias. La API respondió correctamente en el puerto 8082 con el mensaje actualizado.

## Conclusiones

El orden de las instrucciones importa: lo que cambia poco (dependencias) va primero y lo que cambia mucho (código) va al final, así se aprovecha el caché de capas. `.dockerignore` reduce el contexto de construcción y evita copiar archivos sensibles como `.env`.
