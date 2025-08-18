# Deploying ML Models with FastAPI and uv

Este repositorio contiene el código del workshop **"Deploying ML Models with FastAPI and uv"** por **Alexey Grigorev**. 

El workshop enseña cómo implementar y desplegar modelos de machine learning usando FastAPI como framework web y UV como gestor de paquetes moderno para Python. Aprenderás desde el entrenamiento del modelo hasta el deployment en producción.

## Estructura del Proyecto

```
.
├── 01-workshop-uv-fastapi.ipynb    # 📓 Notebook del workshop/tutorial
├── 02-train.py                     # 🎯 Script para entrenar el modelo
├── 03-predict.py                   # 🔮 Script para hacer predicciones
├── 04-ping.py                      # 🏓 Endpoint de health check
├── 05-test.py                      # 🧪 Tests del proyecto
├── Dockerfile                      # 🐳 Configuración Docker
├── README.md                       # 📖 Este archivo
├── fly.toml                        # ✈️ Configuración para Fly.io
├── model_logistic_regression.bin   # 🤖 Modelo entrenado
├── pyproject.toml                  # ⚙️ Configuración del proyecto
└── uv.lock                         # 🔒 Lock file de dependencias
```

## Guía de Navegación

### Para Empezar
1. [**`01-workshop-uv-fastapi.ipynb`**](./01-workshop-uv-fastapi.ipynb) - Comienza aquí si es tu primera vez. Este notebook contiene el tutorial paso a paso.

### Scripts Principales
2. [**`02-train.py`**](./02-train.py) - Ejecuta este script para entrenar tu modelo de regresión logística
3. [**`03-predict.py`**](./03-predict.py) - Usa este script para hacer predicciones con el modelo entrenado
4. [**`04-ping.py`**](./04-ping.py) - Endpoint simple para verificar que la API está funcionando
5. [**`05-test.py`**](./05-test.py) - Ejecuta los tests para verificar que todo funciona correctamente

### Configuración y Deployment
6. [**`pyproject.toml`**](./pyproject.toml) - Configuración del proyecto, dependencias y metadatos
7. [**`uv.lock`**](./uv.lock) - Versiones exactas de las dependencias (generado automáticamente)
8. [**`Dockerfile`**](./Dockerfile) - Para crear una imagen Docker del proyecto
9. [**`fly.toml`**](./fly.toml) - Configuración para deployment en Fly.io

### Modelo
10. [**`model_logistic_regression.bin`**](./model_logistic_regression.bin) - Modelo entrenado listo para usar

## Quick Start - Siguiendo el Workshop

### Pre-requisitos
- Python 3.13+
- Git instalado
- (Opcional) Docker para containerización

### Configuración del entorno
```bash
# Instalar UV si no lo tienes
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias del proyecto
uv sync
```

### Entrenar el Modelo
```bash
uv run python 02-train.py
```

### Levantar la API de predicciones
```bash
uv run python 03-predict.py
```

### Ejecutar Tests
```bash
uv run python 05-test.py
```

## Docker

### Construir la imagen
```bash
docker build -t ml-fastapi-app .
```

### Ejecutar el contenedor
```bash
docker run -p 9696:9696 ml-fastapi-app
```

## Deployment en Fly.io

```bash
# Instalar Fly CLI
curl -L https://fly.io/install.sh | sh

# Login en Fly.io
fly auth login

# Para deployar por primera vez
fly launch --generate-name

# Deployar cambios hechos en el codigo
fly deploy
```

## Sobre el Workshop

Este workshop fue creado por **Alexey Grigorev**, un experto reconocido en MLOps y Machine Learning Engineering. Alexey es:
- Autor de libros sobre Machine Learning
- Organizador de la comunidad DataTalks.Club

El workshop cubre el pipeline completo desde el desarrollo hasta el deployment de modelos ML usando herramientas modernas y mejores prácticas de la industria.

### Objetivos de Aprendizaje:
- Usar UV como gestor de paquetes moderno
- Implementar APIs REST con FastAPI
- Containerizar aplicaciones ML con Docker
- Desplegar modelos en producción con Fly.io
