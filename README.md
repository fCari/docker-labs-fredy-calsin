# Docker Labs - Fredy Calsin

Proyecto práctico: Dockerfile y construcción de imágenes Docker (TECSUP).
Cuatro laboratorios progresivos ejecutados en una VM de Google Compute Engine.

| Lab | Tema | Imagen | Puerto VM |
|---|---|---|---|
| [01](01-nginx-basico/) | Nginx básico | `fredy-calsin-web:v1` | 8080 → 80 |
| [02](02-api-python/) | API FastAPI | `fredy-calsin-api:v1` | 8081 → 8000 |
| [03](03-optimizacion/) | Optimización (caché, `.dockerignore`) | `fredy-calsin-api:v2` | 8082 → 8000 |
| [04](04-seguridad/) | Seguridad (usuario no root) | `fredy-calsin-api:v3` | 8083 → 8000 |

Cada directorio contiene su `Dockerfile`, código, `README.md` y una carpeta `evidencias/` con las capturas.

## Ejecución rápida en la VM

```bash
# Lab 01
cd 01-nginx-basico
docker build -t fredy-calsin-web:v1 .
docker run -d --name fredy-calsin-web -p 8080:80 fredy-calsin-web:v1

# Lab 02
cd ../02-api-python
docker build -t fredy-calsin-api:v1 .
docker run -d --name fredy-calsin-api -p 8081:8000 fredy-calsin-api:v1

# Lab 03
cd ../03-optimizacion
docker build --progress=plain -t fredy-calsin-api:v2 .
docker run -d --name fredy-calsin-api-v2 -p 8082:8000 fredy-calsin-api:v2

# Lab 04
cd ../04-seguridad
docker build -t fredy-calsin-api:v3 .
docker run -d --name fredy-calsin-api-v3 -p 8083:8000 fredy-calsin-api:v3
docker exec fredy-calsin-api-v3 id
```

> El firewall de la VPC debe permitir TCP 8080-8083 hacia la VM.

## Seguridad

No se publican contraseñas, tokens ni archivos `.env` en este repositorio.
