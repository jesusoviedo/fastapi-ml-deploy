from fastapi import FastAPI
import uvicorn

# Importaciones:
# - FastAPI: framework para construir la API
# - uvicorn: servidor ASGI para ejecutar la aplicación


# Inicialización de la aplicación FastAPI
app = FastAPI(title="ping")


@app.get("/ping")
def ping():
    # Endpoint de prueba: responde "PONG" cuando se hace GET a /ping
    return "PONG"


if __name__ == "__main__":
    # Ejecución del servidor en el puerto 9696
    uvicorn.run(app, host="0.0.0.0", port=9696)
