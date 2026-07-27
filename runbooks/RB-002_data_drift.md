# Runbook RB-002
## Data Drift

### Objetivo

Detectar cambios significativos en la distribución de los datos de entrada que puedan afectar el desempeño del modelo de Machine Learning.

---

## Condición de activación

- El script `data_drift.py` detecta variaciones superiores al 30%.
- Se observa una disminución en la calidad de las predicciones.

---

## Diagnóstico

1. Ejecutar:

```bash
python data_drift.py
```

2. Revisar el estado general.

3. Analizar las variables que presentan drift.

4. Validar si el cambio corresponde a una modificación real del proceso industrial.

---

## Acciones

1. Confirmar que los datos sean válidos.
2. Identificar las variables con mayor porcentaje de variación.
3. Evaluar el impacto sobre el modelo.
4. Si el drift compromete el desempeño del modelo:
   - Reentrenar el modelo.
   - O ejecutar el procedimiento RB-003 (Rollback).

---

## Resultado esperado

- Estado general = SIN DATA DRIFT.
- Las variables permanecen dentro del umbral permitido.
- El modelo conserva un desempeño estable.

---

## Evidencia

- Salida de `python data_drift.py`.
- Variables analizadas.
- Captura de la consola.