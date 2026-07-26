# AI4I Predictive Maintenance Platform

1. Introducción

2. Objetivo

3. Arquitectura
## Objetivos del Proyecto
4. Evolución del Proyecto

   Fase 2 Desarrollo del Modelo


   Actividad 6  Evaluación y validación de modelos

   Actividad 7  API de inferencia y despliegue

  
### Fase 3 - Operación del Sistema

- Actividad 8 – Monitoreo y observabilidad
  Funcionalidades implementadas:

  - API de inferencia con FastAPI.
  - Dashboard de monitoreo en Streamlit.
  - Registro de predicciones en monitoring_logs.csv.
  - Trazabilidad mediante Trace ID.
  - Monitoreo de latencia.
  - Indicadores SLO (Service Level Objective).
  - Error Budget.
  - Detección de Data Drift.
  - Procedimiento de Rollback del modelo.
  - Integración con MLflow para seguimiento de experimentos.
  - Runbooks operativos para incidentes.

- Actividad 9 – Escalabilidad, FinOps y Gobernanza
- Resultado Final – Pipeline MLOps + GitOps


## 5. Stack Tecnológico

| Componente | Herramienta |
|------------|-------------|
| Lenguaje | Python 3.13 |
| API | FastAPI |
| Dashboard | Streamlit |
| Machine Learning | Scikit-Learn |
| Modelo desplegado | Random Forest (modelo.pkl) |
| Serialización | Joblib (.pkl) |
| Monitoreo | Monitoring Logs + Streamlit |
| Observabilidad | Trace ID |
| Experiment Tracking | MLflow |
| Versionamiento | Git + GitHub |
| Repositorio | GitHub |
| Contenedores | Docker |
| Pruebas | Pytest |
| Gestión de datos | Pandas |
| Visualización | Plotly |

6. Arquitectura
                    Usuario
                       │
                       ▼
              FastAPI (app.py)
                       │
             Predicción del modelo
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
monitoring_logs   data_drift.py   MLflow
      │                │              │
      ▼                ▼              ▼
Dashboard        Drift Detection  Experimentos
(Streamlit)             │
      │                 ▼
      │          rollback_model.py
      │                 │
      └─────────────────┘
               Recuperación

7. Cómo ejecutar
## 7. Cómo ejecutar

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar la API

```bash
uvicorn app:app --reload
```

### Ejecutar el Dashboard

```bash
streamlit run dashboard_monitoring.py
```

### Ejecutar Data Drift

```bash
python data_drift.py
```

### Ejecutar Rollback

```bash
python rollback_model.py
```

### Ejecutar MLflow

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000
```

8. Evidencias
## 8. Evidencias

Durante el desarrollo de la Actividad 8 se implementaron y validaron las siguientes funcionalidades:

- Dashboard de monitoreo en Streamlit.
- Registro histórico de predicciones.
- Trazabilidad mediante Trace ID.
- Monitoreo de latencia.
- Indicadores SLO y Error Budget.
- Detección de Data Drift.
- Procedimiento de Rollback del modelo.
- Integración con MLflow.
- Runbooks operativos para incidentes.

9. Resultados

## 9. Conclusiones

Se implementó una plataforma de monitoreo para un modelo de Machine Learning que incorpora observabilidad, trazabilidad, detección de Data Drift, procedimientos de recuperación mediante Rollback y seguimiento de experimentos con MLflow. Esta solución constituye la base para la siguiente etapa del proyecto, enfocada en escalabilidad, FinOps, gobernanza y automatización MLOps.

10. Roadmap
