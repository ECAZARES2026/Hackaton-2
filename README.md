
# Actividad 6 - Evaluación y Validación de Modelos

## Integrantes
- Erika Cazarez
- Luis Flores
- Juan Arizmendi

## Dataset
AI4I 2020 Predictive Maintenance Dataset

## Modelos Evaluados
- Logistic Regression
- Random Forest
- XGBoost

## Técnicas Aplicadas
- Matriz de Confusión
- ROC-AUC
- Grid Search
- Validación Cruzada
- Ajuste de Umbral
- Prueba A/B

## Resultados

| Modelo | Accuracy | Recall | F1 Score | ROC-AUC |
|----------|----------:|----------:|----------:|----------:|
| Logistic Regression | 0.9685 | 0.1471 | 0.2409 | 0.9000 |
| Random Forest | 0.9825 | 0.5735 | 0.6903 | 0.9638 |
| XGBoost | 0.9855 | 0.6912 | 0.7642 | 0.9725 |

## Modelo Seleccionado

XGBoost con ajuste de umbral a 0.30.

## Archivos

- Notebook: PM_AI4I_rev_2_MLOps_actividad_6.ipynb
- Dashboard: dashboard_modelos.png

- ## Conclusiones

Durante esta actividad se evaluaron tres modelos de clasificación para la predicción de fallas en equipos industriales utilizando el dataset **AI4I 2020 Predictive Maintenance Dataset**.

Los resultados mostraron que **Logistic Regression** obtuvo una alta exactitud, pero presentó un Recall bajo, lo que indica una capacidad limitada para detectar fallas reales. Por su parte, **Random Forest** mejoró significativamente la detección de fallas y ofreció un mejor equilibrio entre precisión y sensibilidad.

El modelo **XGBoost** obtuvo el mejor desempeño global, alcanzando los valores más altos de Recall, F1 Score y ROC-AUC, demostrando una mayor capacidad para identificar correctamente los eventos de falla sin afectar significativamente la precisión del modelo.

Mediante la aplicación de **Grid Search** y **Validación Cruzada**, se confirmó la estabilidad y capacidad de generalización del modelo seleccionado. Posteriormente, el **ajuste de umbral** y la **prueba A/B** permitieron incrementar el Recall de **69.12% a 76.47%**, aumentando la detección de fallas reales y reduciendo los falsos negativos.

Con base en los resultados obtenidos, se concluye que **XGBoost con un umbral optimizado de 0.30** representa la mejor alternativa para una posible implementación en escenarios de mantenimiento predictivo, ya que ofrece el mejor equilibrio entre desempeño estadístico y valor operativo para la detección temprana de fallas.

## Autores
Equipo Tecmilenio 2026
