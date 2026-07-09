# Fase II
## Despliegue de una API de Machine Learning con FastAPI, Docker y Render

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Render](https://img.shields.io/badge/Render-Cloud-purple)
![License](https://img.shields.io/badge/License-Educational-orange)

---

# 👩‍💻 Autor

**Erika Cazares **

Máster en Inteligencia Artificial – Tecmilenio

---

# 📌 Objetivo

Desarrollar y desplegar una API REST para un modelo de Machine Learning utilizando FastAPI, contenerizar la aplicación mediante Docker y publicarla en la nube usando Render para realizar inferencias desde cualquier dispositivo con acceso a Internet.

---

# 🏗 Arquitectura del proyecto

```text
                Dataset AI4I
                      │
                      ▼
          Entrenamiento del Modelo
                      │
                      ▼
                 modelo.pkl
                      │
                      ▼
                  FastAPI
                      │
                      ▼
                   Docker
                      │
                      ▼
                  GitHub
                      │
                      ▼
             Render (Cloud)
                      │
                      ▼
        API pública disponible 24/7*
```

\*En el plan gratuito de Render la instancia entra en reposo tras un periodo de inactividad y se reactiva automáticamente cuando recibe una nueva solicitud.

---

# 🛠 Tecnologías utilizadas

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- Git
- GitHub
- Render
- Scikit-Learn
- XGBoost
- Swagger / OpenAPI

---

# 📂 Estructura del proyecto

```
Hackaton-2
│
├── app.py
├── modelo.pkl
├── Dockerfile
├── requirements.txt
├── README.md
├── ai4i2020.csv
├── dashboard_modelos.png
├── .gitignore
└── .dockerignore
```

---

# 🌐 API pública

## URL principal

https://hackaton-2-qlp5.onrender.com

---

## Documentación Swagger

https://hackaton-2-qlp5.onrender.com/docs

---

# 📡 Endpoint disponible

## GET /

Verifica que la API está activa.

Respuesta:

```json
{
    "mensaje":"API mexa de predicción de fallas CDU activa 🇲🇽"
}
```

---

## POST /predict

Realiza la predicción utilizando el modelo de Machine Learning.

### Ejemplo de entrada

```json
{
  "Type":0,
  "Air_temperature_K":304,
  "Process_temperature_K":313,
  "Rotational_speed_rpm":1200,
  "Torque_Nm":65,
  "Tool_wear_min":220
}
```

### Ejemplo de salida

```json
{
    "probabilidad_falla":0.9817,
    "umbral":0.3,
    "prediccion":1,
    "resultado":"Riesgo de falla"
}
```

---

# 🔄 Flujo del despliegue

1. Entrenamiento del modelo.
2. Exportación del modelo (`modelo.pkl`).
3. Desarrollo de la API con FastAPI.
4. Contenerización mediante Docker.
5. Versionamiento con Git.
6. Publicación en GitHub.
7. Despliegue automático en Render.
8. Publicación de la API en Internet.

---

# ✅ Resultado

Se logró desplegar exitosamente una API REST para realizar inferencias de Machine Learning desde cualquier navegador mediante una URL pública.

La API responde correctamente utilizando el modelo entrenado y permite realizar predicciones a través de Swagger/OpenAPI.

---

# 📷 Evidencia

El despliegue fue validado mediante:

- API pública funcionando.
- Swagger disponible.
- Predicciones realizadas correctamente.
- Despliegue automático desde GitHub mediante Render.

---

# 🎓 Proyecto académico

Actividad desarrollada como parte del Máster en Inteligencia Artificial del Tecnológico de Monterrey (Tecmilenio), enfocada en el despliegue de modelos de Machine Learning mediante prácticas de MLOps.

## Agradecimientos

Este proyecto fue desarrollado por **Erika Cazarez**, con el apoyo de ChatGPT como asistente técnico para revisión de código, documentación y acompañamiento durante el proceso de desarrollo.
