from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hola desde mi API Docker",
        "student": "Fredy Calsin",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
