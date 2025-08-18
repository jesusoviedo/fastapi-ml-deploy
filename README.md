# 🚀 Implementación de Modelos de ML con FastAPI y uv

> **Notebook educativo completo para aprender a deployar modelos de Machine Learning usando las herramientas más modernas de Python**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)](https://fastapi.tiangolo.com/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Fly.io](https://img.shields.io/badge/Deploy-Fly.io-purple.svg)](https://fly.io/)

## 📖 Descripción

Este repositorio contiene un **notebook educativo completo** que te enseña a implementar y desplegar modelos de Machine Learning en producción usando las herramientas más modernas y eficientes del ecosistema Python.

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
├── README.md                        # Este archivo
├── notebook/                        # 📓 Notebook educativo principal
│   ├── ml_fastapi_deployment.md     # Guía completa paso a paso
│   └── workshop_fastapi_ml/         # 📂 Archivos guardados del workshop original
├── raw/                             # 📝 Material fuente
│   └── video_notes.md               # Notas del workshop original
└── .gitignore                       # Archivos ignorados por Git
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

- Python 3.11 o superior
- [UV](https://github.com/astral-sh/uv) instalado
- Docker (opcional, para contenedorización)
- Cuenta en [Fly.io](https://fly.io/) (opcional, para deployment)

### Instalación

```bash
# 1. Clonar el repositorio
git clone <tu-repo-url>
cd ml-fastapi-uv

# 2. Instalar UV (si no lo tienes)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Abrir el notebook educativo
# Recomendado: VS Code, Jupyter Lab, o cualquier editor Markdown
```

### 📓 Seguir el Notebook

El notebook principal (`notebook/ml-fastapi-uv.md`) está diseñado para ser seguido paso a paso:

1. **📖 Lee cada sección cuidadosamente** - Contiene explicaciones detalladas
2. **💻 Ejecuta el código** - Todos los ejemplos son funcionales
3. **🧪 Experimenta** - Modifica parámetros y observa los resultados
4. **🎯 Completa el proyecto** - Al final tendrás una API completa

## 🎬 Fuente Original

Este material educativo está basado en el excelente workshop de **Alexey Grigorev**:

**🎥 Video Original:** [Deploying ML Models with FastAPI and uv](https://www.youtube.com/watch?v=jzGzw98Eikk)

### 📝 Contenido Ampliado

El notebook expande significativamente el contenido original con:
- **Explicaciones pedagógicas detalladas** de cada concepto
- **Ejemplos de código completos y funcionales**
- **Mejores prácticas actualizadas** para 2024-2025
- **Secciones de troubleshooting y optimización**
- **Referencias adicionales y recursos complementarios**

## 📚 Recursos y Enlaces de Interés

### 🔗 Enlaces del Workshop Original

- **Code for this Workshop:** https://github.com/alexeygrigorev/workshop-fastapi-uv
- **ML Zoomcamp Course Content:** https://github.com/DataTalksClub/machine-learning-zoomcamp
- **Module 5 of ML Zoomcamp:** https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment

### 📖 Documentación Oficial

- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **UV Documentation:** https://docs.astral.sh/uv/
- **Pydantic Documentation:** https://docs.pydantic.dev/
- **Fly.io Documentation:** https://fly.io/docs/
- **Scikit-learn User Guide:** https://scikit-learn.org/stable/user_guide.html

### 🎥 Videos Recomendados

- **FastAPI Tutorial Series:** [Playlist de FastAPI](https://www.youtube.com/playlist?list=PLQhWOGWWcV6KLXgSwN2EFWLLXk9T3uTiq)
- **ML Zoomcamp Complete Course:** [DataTalks.Club YouTube](https://www.youtube.com/c/DataTalksClub)
- **Python Packaging with UV:** [Charming Data](https://www.youtube.com/watch?v=8UuW8o4bHbw)
- **Docker for Python Developers:** [Tech With Tim](https://www.youtube.com/watch?v=bi0cKgmRuiA)

### 🎓 Cursos Complementarios

#### **Gratuitos**
- **ML Zoomcamp:** [Complete Free Course](https://github.com/DataTalksClub/machine-learning-zoomcamp) - Curso completo de ML
- **FastAPI Course:** [FreeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA) - 19 horas de FastAPI
- **Python API Development:** [Academind](https://www.youtube.com/watch?v=0tV0s8ajpQk) - Desarrollo de APIs

#### **Pagos**
- **FastAPI for Beginners:** [Udemy](https://www.udemy.com/course/fastapi-the-complete-course/) - Curso completo
- **MLOps Specialization:** [Coursera](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) - MLOps con Andrew Ng
- **Python Web APIs:** [Pluralsight](https://www.pluralsight.com/paths/python-web-development) - Desarrollo web Python

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

Si tienes preguntas o sugerencias sobre este material educativo:

- **GitHub Issues:** Para reportar bugs o solicitar features
- **Discussions:** Para preguntas generales y discusiones

---

**¡Esperamos que este material te ayude a dominar el deployment de modelos ML con las herramientas más modernas! 🚀**

---

*Última actualización: Agosto 2025*