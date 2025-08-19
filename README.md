# 🚀 Implementación de Modelos de ML con FastAPI y uv

> **Repositorio educativo completo para aprender a deployar modelos de Machine Learning usando las herramientas más modernas de Python**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)](https://fastapi.tiangolo.com/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Fly.io](https://img.shields.io/badge/Deploy-Fly.io-purple.svg)](https://fly.io/)

## 📖 Descripción

Este repositorio contiene recursos educativos completos que te enseñan a implementar y desplegar modelos de Machine Learning en producción usando las herramientas más modernas y eficientes del ecosistema Python.

### 🎯 Objetivo

Aprender a crear una **API robusta y escalable** para servir modelos de ML, siguiendo las mejores prácticas de MLOps y usando tecnologías de vanguardia que representan el estado del arte en 2024-2025.

### 🔧 Stack Tecnológico

- **🐍 Python 3.13+**: Lenguaje base con las últimas características
- **⚡ FastAPI**: Framework web moderno y ultra-rápido
- **📦 UV**: Gestor de dependencias escrito en Rust (10x más rápido que pip)
- **🤖 Scikit-learn**: Machine Learning con pipelines optimizados
- **🔍 Pydantic**: Validación automática de datos con type hints
- **🐳 Docker**: Contenedorización para deployment consistente
- **☁️ Fly.io**: Plataforma de deployment moderna y global

## 📁 Estructura del Proyecto

```
.
├── fastapi_ml_deployment_guide.ipynb    # 📚 Guía completa de deployment ML
└── workshop_fastapi_ml/                 # 🎓 Workshop práctico completo
    ├── 01-workshop-uv-fastapi.ipynb     # 📓 Tutorial paso a paso
    ├── 02-train.py                      # 🎯 Entrenamiento del modelo
    ├── 03-predict.py                    # 🔮 Sistema de predicciones
    ├── 04-ping.py                       # 🏓 Health check endpoint
    ├── 05-test.py                       # 🧪 Tests automatizados
    ├── Dockerfile                       # 🐳 Containerización
    ├── README.md                        # 📖 Documentación técnica detallada
    ├── fly.toml                         # ✈️ Configuración Fly.io
    ├── model_logistic_regression.bin    # 🤖 Modelo entrenado
    ├── pyproject.toml                   # ⚙️ Configuración proyecto
    └── uv.lock                          # 🔒 Dependencies lock
```

## 🎓 ¿Qué Aprenderás?

### 1. **Gestión Moderna de Proyectos Python**
- Configuración con **UV** (alternativa ultrarrápida a pip/pipenv)
- Archivo `pyproject.toml` para definición completa del proyecto
- Gestión de dependencias y entornos virtuales eficiente

### 2. **Machine Learning Pipeline Robusto**
- Entrenamiento de modelo de **predicción de churn** de clientes
- Uso de **scikit-learn pipelines** para consistencia
- Preprocesamiento con `DictVectorizer`
- Guardado y carga eficiente de modelos con `joblib`

### 3. **API de Producción con FastAPI**
- Creación de endpoints RESTful optimizados
- **Documentación automática** con Swagger UI
- Validación de datos con **Pydantic**
- Manejo de errores y logging estructurado
- Health checks y monitoreo

### 4. **Deployment y DevOps**
- **Contenedorización** con Docker multi-stage
- Deployment en **Fly.io** con configuración optimizada
- Testing automatizado con **pytest**
- Mejores prácticas de seguridad y rendimiento

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.13 o superior
- [UV](https://github.com/astral-sh/uv) instalado
- Docker (opcional, para contenedorización)
- Cuenta en [Fly.io](https://fly.io/) (opcional, para deployment)

### 📍 ¿Por Dónde Empezar?

#### 📖 **Opción 1: Conceptos y Teoría**
```bash
# Clonar el repositorio
git clone https://github.com/jesusoviedo/fastapi-ml-deploy.git
cd fastapi-ml-deploy

# Abrir la guía completa de deployment
jupyter notebook fastapi_ml_deployment_guide.ipynb
```

**👉 Perfecto para**: Entender conceptos fundamentales, arquitecturas y mejores prácticas.

#### 🛠️ **Opción 2: Práctica Hands-On Directa**
```bash
# Clonar el repositorio
git clone https://github.com/jesusoviedo/fastapi-ml-deploy.git
cd fastapi-ml-deploy/workshop_fastapi_ml

# Instalar UV (si no lo tienes)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Seguir el workshop paso a paso
jupyter notebook 01-workshop-uv-fastapi.ipynb

# O leer la documentación técnica
cat README.md
```

**👉 Perfecto para**: Implementar y desplegar inmediatamente una API funcional.

### 🎯 Rutas de Aprendizaje Recomendadas

#### 🔰 **Principiante en ML Deployment**
1. **📚 Teoría primero** → `fastapi_ml_deployment_guide.ipynb`
2. **📓 Tutorial interactivo** → `workshop_fastapi_ml/01-workshop-uv-fastapi.ipynb`
3. **🛠️ Implementación** → Seguir archivos `02-train.py` a `05-test.py`
4. **🚀 Deployment** → `Dockerfile` y `fly.toml`

#### ⚡ **Desarrollador Experimentado**
1. **🔍 Revisión rápida** → `fastapi_ml_deployment_guide.ipynb` (secciones avanzadas)
2. **💻 Implementación directa** → `workshop_fastapi_ml/02-train.py` y siguientes
3. **🐳 Containerización** → `workshop_fastapi_ml/Dockerfile`
4. **☁️ Deploy inmediato** → `workshop_fastapi_ml/fly.toml`

> 💡 **Nota**: La carpeta `workshop_fastapi_ml` contiene su propio `README.md` con **instrucciones técnicas detalladas** para ejecutar cada paso.

## 🎬 Fuente Original

Este material educativo está basado en el excelente workshop de **Alexey Grigorev**:

**🎥 Video Original:** [Deploying ML Models with FastAPI and uv](https://www.youtube.com/watch?v=jzGzw98Eikk)

### 📝 Contenido Ampliado

El repositorio expande significativamente el contenido original con:
- **Explicaciones pedagógicas detalladas** de cada concepto
- **Guía completa de deployment** con teoría y práctica
- **Ejemplos de código completos y funcionales**
- **Mejores prácticas actualizadas** para 2024-2025
- **Secciones de troubleshooting y optimización**
- **Referencias adicionales y recursos complementarios**

## 📚 Recursos y Enlaces de Interés

### 🔗 Enlaces del Workshop Original

- **Code for this Workshop:** https://github.com/alexeygrigorev/workshops/tree/main/mlzoomcamp-fastapi-uv
- **ML Zoomcamp Course Content:** https://github.com/DataTalksClub/machine-learning-zoomcamp
- **Module 5 of ML Zoomcamp:** https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment

### 📖 Documentación Oficial

- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **UV Documentation:** https://docs.astral.sh/uv/
- **Pydantic Documentation:** https://docs.pydantic.dev/
- **Fly.io Documentation:** https://fly.io/docs/
- **Scikit-learn User Guide:** https://scikit-learn.org/stable/user_guide.html

### 🎥 Videos Recomendados

- **FastAPI para IA:** [Cree un punto final de IA en 30 minutos](https://www.youtube.com/watch?v=uDUfZyNXFX0)
- **ML Zoomcamp Complete Course:** [DataTalks.Club YouTube](https://www.youtube.com/c/DataTalksClub)
- **Python Packaging with UV:** [Charming Data](https://www.youtube.com/watch?v=8UuW8o4bHbw)
- **Docker for Python Developers:** [Tech With Tim](https://www.youtube.com/watch?v=bi0cKgmRuiA)

### 🎓 Cursos Complementarios

- **ML Zoomcamp:** [Complete Free Course](https://github.com/DataTalksClub/machine-learning-zoomcamp) - Curso completo de ML
- **FastAPI Course:** [FreeCodeCamp](https://www.youtube.com/watch?v=tLKKmouUams) - 1 hora de FastAPI
- **Python API Development:** [Academind](https://www.youtube.com/watch?v=0tV0s8ajpQk) - Desarrollo de APIs
- **FastAPI for Beginners:** [Udemy](https://www.udemy.com/course/fastapi-the-complete-course/) - Curso completo
- **MLOps Specialization:** [Coursera](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) - MLOps con Andrew Ng
- **FastAPI Courses:** [Pluralsight](https://www.pluralsight.com/browse?=&q=fastapi&sort=relevance&page=1) - FastAPI cursos

### 🛠️ Herramientas y Librerías Relacionadas

- **MLflow:** [Tracking y Model Registry](https://mlflow.org/)
- **Streamlit:** [Apps web para ML](https://streamlit.io/)
- **Gradio:** [Interfaces rápidas para ML](https://gradio.app/)
- **BentoML:** [Framework de ML Serving](https://bentoml.org/)
- **Ray Serve:** [Escalado de ML models](https://docs.ray.io/en/latest/serve/)

### 📊 Datasets para Práctica

- **Customer Churn Datasets:** [Kaggle](https://www.kaggle.com/datasets?search=customer+churn)
- **Telco Customer Churn:** [IBM Sample Data](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **UCI ML Repository:** [Datasets clásicos](https://archive.ics.uci.edu/ml/index.php)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores, tienes sugerencias o quieres añadir contenido:

1. **Fork** el repositorio
2. **Crea** una rama para tu feature (`git checkout -b feature/mejora-increible`)
3. **Commit** tus cambios (`git commit -m 'Añadir mejora increíble'`)
4. **Push** a la rama (`git push origin feature/mejora-increible`)
5. **Abre** un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🙏 Agradecimientos

- **Alexey Grigorev** por el workshop original y la inspiración
- **DataTalks.Club** por promover educación ML gratuita y de calidad
- **Comunidad FastAPI** por crear un framework excepcional
- **Astral Team** por UV y las herramientas modernas de Python

---

## 📬 Contacto

**Mantenedor:** [@jesusoviedo](https://github.com/jesusoviedo)

Si tienes preguntas o sugerencias sobre este material educativo:

- **GitHub Issues:** Para reportar bugs o solicitar features
- **Discussions:** Para preguntas generales y discusiones

---

**¡Esperamos que este material te ayude a dominar el deployment de modelos ML con las herramientas más modernas! 🚀**

---

*Última actualización: Agosto 2025*