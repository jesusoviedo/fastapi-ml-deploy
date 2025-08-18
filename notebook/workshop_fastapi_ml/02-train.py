#!/usr/bin/env python

# --- Importacion de Librerías ---
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction import  DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# --- Verificacion de Versiones ---
print(f'pandas=={pd.__version__}')
print(f'numpy=={np.__version__}')
print(f'sklearn=={sklearn.__version__}')


# --- Funcion para Cargar y Preparar los Datos ---
def load_data():
    """
    Esta función descarga los datos de una URL, los limpia y los prepara para el entrenamiento
    """

    data_url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-03-churn-prediction/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    df = pd.read_csv(data_url)

    # Limpieza de los Nombres de las Columnas
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Identificamos las columnas que contienen texto (tipo 'object')
    categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

    # Limpieza de los Datos Categóricos
    for c in categorical_columns:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    # Limpieza de la Columna 'totalcharges'
    df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
    df.totalcharges = df.totalcharges.fillna(0)

    # Preparacion de la Variable Objetivo
    df.churn = (df.churn == 'yes').astype(int)

    # Devolvemos el DataFrame limpio y listo para usarse
    return df


# --- Funcion para Entrenar el Modelo ---
def train_model(df):
    """
    Esta función entrena un modelo de regresión logística usando un pipeline.
    """
    # Definimos las columnas numéricas y categoricas que usaremos como características.
    numerical = ['tenure', 'monthlycharges', 'totalcharges']

    categorical = [
        'gender',
        'seniorcitizen',
        'partner',
        'dependents',
        'phoneservice',
        'multiplelines',
        'internetservice',
        'onlinesecurity',
        'onlinebackup',
        'deviceprotection',
        'techsupport',
        'streamingtv',
        'streamingmovies',
        'contract',
        'paperlessbilling',
        'paymentmethod',
    ]

    y_train = df.churn
    # Creamos un diccionario con las características (features) para entrenar el modelo.
    train_dict = df[categorical + numerical].to_dict(orient='records')

    # Creacion del Pipeline de Entrenamiento
    pipeline = make_pipeline(
        DictVectorizer(),
        LogisticRegression(solver='liblinear')
    )

    # Entrenamos el pipeline
    pipeline.fit(train_dict, y_train)

    # Devolvemos el pipeline
    return pipeline


# --- Funcion para Guardar el Modelo ---
def save_model(pipeline, output_file):
    """
    Guarda el pipeline entrenado en un archivo usando pickle.
    """

    # Abrimos un archivo en modo de escritura binaria ('wb')
    with open(output_file, 'wb') as f_out:
        pickle.dump(pipeline, f_out)

    print(f'Model saved to {output_file}')

# --- Bloque Principal de Ejecución ---
# 1. Cargamos y preparamos los datos
df = load_data()

# 2. Entrenamos el modelo con los datos
pipeline = train_model(df)

# 3. Guardamos el modelo entrenado en un archivo llamado 'model.bin'.
save_model(pipeline, 'model_logistic_regression.bin')