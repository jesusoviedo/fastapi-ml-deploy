import pickle
from typing import Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI
import uvicorn

# 📌 Importaciones necesarias:
# - pickle: para cargar el modelo entrenado
# - typing.Literal: para validar valores estrictos de entrada
# - pydantic.BaseModel & Field: para definir y validar esquemas de datos
# - FastAPI: framework para crear la API
# - uvicorn: servidor ASGI para ejecutar la aplicación


class Customer(BaseModel):
    # Modelo de entrada: define el esquema del cliente con validaciones de tipos
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)               # Debe ser mayor o igual a 0
    monthlycharges: float = Field(..., ge=0.0)   # Debe ser >= 0.0
    totalcharges: float = Field(..., ge=0.0)     # Debe ser >= 0.0


class PredictResponse(BaseModel):
    # Modelo de salida: define la estructura de la respuesta
    churn_probability: float
    churn: bool


# Inicialización de la aplicación FastAPI
app = FastAPI(title="customer-churn-prediction")

# Cargar el pipeline entrenado desde archivo binario
with open('model_logistic_regression.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    # Función auxiliar: calcula la probabilidad de churn para un cliente
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    # Endpoint principal: recibe un cliente, calcula churn y devuelve respuesta
    prob = predict_single(customer.model_dump())

    return PredictResponse(
        churn_probability=prob,
        churn=prob >= 0.5
    )


if __name__ == "__main__":
    # Ejecuta el servidor Uvicorn en el puerto 9696
    uvicorn.run(app, host="0.0.0.0", port=9696)
