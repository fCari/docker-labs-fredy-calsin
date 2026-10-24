from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hola desde mi API Docker segura",
        "student": "Fredy Calsin 3",
        "version": "3.0"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
