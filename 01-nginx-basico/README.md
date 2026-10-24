# Laboratorio 01 - Primera imagen Docker

## Datos del alumno

**Nombre:** Fredy Calsin
**Imagen:** fredy-calsin-web:v1
**Puerto:** 8080

## Objetivo

Crear una imagen Docker personalizada usando Nginx que publique una página HTML con el nombre completo del alumno.

## Procedimiento

### 1. Construcción de la imagen

```bash
docker build -t fredy-calsin-web:v1 .
docker images
```

### 2. Ejecución del contenedor

```bash
docker run -d --name fredy-calsin-web \
  -p 8080:80 fredy-calsin-web:v1
```

### 3. Comprobación

```bash
curl http://localhost:8080
# Desde otro equipo: http://IP_PUBLICA_VM:8080
```

## Explicación del Dockerfile

| Instrucción | Finalidad |
|---|---|
| `FROM nginx:stable-alpine` | Selecciona la imagen base de Nginx (versión estable sobre Alpine, liviana). |
| `COPY index.html ...` | Incorpora el HTML al directorio web que sirve Nginx. |

## Evidencias

### Imagen Docker construida

![Construcción](evidencias/01-build.png)

### Contenedor funcionando

![Aplicación web](evidencias/02-web.png)

## Resultado

Se construyó la imagen `fredy-calsin-web:v1`, se ejecutó el contenedor publicando el puerto 8080 de la VM hacia el puerto 80 del contenedor y la página mostró correctamente el nombre "Fredy Calsin".

## Conclusiones

`docker build` genera una imagen a partir de un Dockerfile y `docker run` crea un contenedor desde ella. Aprendí a personalizar una imagen base copiando mis propios archivos y a publicar un puerto con `-p`.
