Video: [Deploying ML Models with FastAPI and uv - Alexey Grigorev](https://www.youtube.com/watch?v=jzGzw98Eikk)

Apuntes del video:

### **Taller: Implementación de Modelos de ML con FastAPI y uv**

Este taller, parte del curso "Machine Learning Zoomcamp", se enfoca en la ingeniería de Machine Learning. El objetivo principal es actualizar el Módulo 5 del curso, introduciendo herramientas más modernas y eficientes para la implementación de modelos de Machine Learning.

---

### **Herramientas y Tecnologías**

* **FastAPI:** Reemplaza a Flask para la creación de servicios web. Es más rápido y popular.
* **UV:** Una alternativa a `pipenv` para la gestión de dependencias y entornos virtuales. Es mucho más rápido al estar escrito en Rust.
* **Docker:** Se utilizarán imágenes de Docker actualizadas para incluir las nuevas librerías.
* **fly.io:** Una plataforma para desplegar modelos en la nube, como alternativa a AWS Elastic Beanstalk.

---

### **Flujo de Trabajo**

1.  **Configuración del Entorno:** Se recomienda utilizar Code Spaces de GitHub para tener un entorno preconfigurado con Docker y Python.
2.  **Entrenamiento y Guardado del Modelo:**
    * **Caso de uso:** Predecir la "rotación de clientes" (churn).
    * **Preprocesamiento:** Se utiliza `DictionaryVectorizer` para convertir los datos categóricos en un formato numérico.
    * **Modelo:** Se entrena un modelo de `LogisticRegression`.
    * **Guardado:** Se utiliza `pickle` para guardar el modelo entrenado y el vectorizador en un archivo.
3.  **Mejora con Pipelines de scikit-learn:**
    * Se utiliza `make_pipeline` para combinar el `DictionaryVectorizer` y el `LogisticRegression` en un solo objeto.
    * Esto simplifica el entrenamiento y el guardado del modelo.
4.  **Creación de un Servicio Web con FastAPI:**
    * Se crea un script `predict.py` para cargar el modelo y exponerlo a través de un endpoint de API.
    * El endpoint recibe los datos del cliente y devuelve la probabilidad de churn.
    * FastAPI genera automáticamente documentación interactiva (Swagger UI).
5.  **Validación de Entrada con Pydantic:**
    * Se utilizan modelos de Pydantic para definir la estructura y el tipo de los datos de entrada y salida.
    * Esto mejora la robustez del servicio al validar automáticamente las solicitudes.
6.  **Gestión de Dependencias con UV:**
    * Se utiliza `uv` para crear un entorno virtual y gestionar las dependencias del proyecto.
    * `uv init` crea un archivo `pyproject.toml` para definir las dependencias.
    * `uv add` instala las dependencias en el entorno virtual.
7.  **Contenerización con Docker:**
    * Se crea un `Dockerfile` para empaquetar la aplicación y sus dependencias en una imagen de Docker.
    * La imagen se construye y se ejecuta en un contenedor.
8.  **Despliegue a la Nube con fly.io:**
    * Se utiliza `flyctl` para desplegar la imagen de Docker en la plataforma fly.io.
    * Esto hace que el servicio web sea accesible a través de una URL pública.

---

### **Conceptos Clave**

* **API (Interfaz de Programación de Aplicaciones):** Permite que diferentes aplicaciones se comuniquen entre sí. En este caso, FastAPI se utiliza para crear una API que expone el modelo de Machine Learning.
* **Entorno Virtual:** Un entorno aislado que contiene las dependencias de un proyecto específico. Esto evita conflictos de versiones entre diferentes proyectos.
* **Contenedor:** Una unidad de software que empaqueta el código y todas sus dependencias. Los contenedores de Docker son portátiles y se pueden ejecutar en cualquier lugar.
* **Pipeline de scikit-learn:** Una forma de encadenar múltiples pasos de preprocesamiento y modelado en un solo objeto. Esto simplifica el flujo de trabajo de Machine Learning.
* **Pydantic:** Una librería de Python para la validación de datos. Se integra con FastAPI para validar las solicitudes y respuestas de la API.