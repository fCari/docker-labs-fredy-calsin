# Laboratorio 02 - Dockerizar una API con FastAPI

## Datos del alumno

**Nombre:** Fredy Calsin
**Imagen:** fredy-calsin-api:v1
**Puerto:** 8081

## Objetivo

Construir una imagen Docker que instale las dependencias de Python y ejecute una API FastAPI con endpoints verificables.

## Procedimiento

### 1. Construcción de la imagen

```bash
docker build -t fredy-calsin-api:v1 .
docker images
```

### 2. Ejecución del contenedor

```bash
docker run -d \
  --name fredy-calsin-api \
  -p 8081:8000 \
  fredy-calsin-api:v1
```

### 3. Prueba de los endpoints

```bash
curl http://localhost:8081/
curl http://localhost:8081/health
# Documentación interactiva: http://IP_PUBLICA_VM:8081/docs
```

## Explicación de las instrucciones del Dockerfile

| Instrucción | Finalidad |
|---|---|
| `FROM python:3.12-slim` | Selecciona Python como imagen base (variante liviana). |
| `WORKDIR /app` | Define el directorio de trabajo dentro de la imagen. |
| `COPY requirements.txt .` / `COPY main.py .` | Incorpora las dependencias y el código fuente. |
| `RUN pip install --no-cache-dir ...` | Instala los paquetes al construir la imagen. |
| `EXPOSE 8000` | Documenta el puerto en el que escucha la aplicación. |
| `CMD [...]` | Establece cómo inicia el proceso principal (uvicorn). |

### ¿Por qué `--no-cache-dir`?

Es una opción de **pip** que evita conservar su caché de descargas después de instalar los paquetes, reduciendo el tamaño de la imagen. No es lo mismo que `docker build --no-cache`, que deshabilita la reutilización del caché de construcción de Docker.

## Evidencias

### Imagen construida

![Imagen construida](evidencias/01-build.png)

### Respuesta JSON del endpoint `/`

![Endpoint raíz](evidencias/02-root.png)

### Documentación automática en `/docs`

![Swagger docs](evidencias/03-docs.png)

## Resultado

La imagen `fredy-calsin-api:v1` se construyó correctamente. El endpoint `/` devolvió un JSON con el nombre "Fredy Calsin", `/health` respondió `{"status": "ok"}` y la documentación interactiva estuvo disponible en `/docs`.

## Conclusiones

Aprendí a dockerizar una aplicación Python: copiar primero las dependencias, instalarlas y luego copiar el código, además de la diferencia entre `EXPOSE` (documenta) y `-p` (publica el puerto).
