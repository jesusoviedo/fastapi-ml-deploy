# Usar una imagen base ligera de Python 3.13
FROM python:3.13.5-slim-bookworm

# Copiar la herramienta uv desde otra imagen para manejar dependencias
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /code

# Añadir la carpeta de entorno virtual al PATH
ENV PATH="/code/.venv/bin:$PATH"

# Copiar archivos de configuración del proyecto
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Instalar dependencias con uv (usando lock para versiones fijas)
RUN uv sync --locked

# Copiar el archivo predict.py y el modelo entrenado
COPY "03-predict.py" "model_logistic_regression.bin" ./

# Exponer el puerto 9696 para la API
EXPOSE 9696

# Definir el comando de inicio: ejecutar uvicorn para levantar la API
ENTRYPOINT ["uvicorn", "03-predict:app", "--host", "0.0.0.0", "--port", "9696"]
