# Runbook RB-003
## Rollback del Modelo

### Objetivo

Restaurar la última versión estable del modelo de Machine Learning cuando el modelo desplegado presente un desempeño deficiente.

---

## Condición de activación

- Data Drift confirmado.
- Disminución significativa en la precisión del modelo.
- Incremento de falsos positivos o falsos negativos.
- Validación del equipo de operación.

---

## Diagnóstico

1. Confirmar que el modelo presenta degradación.
2. Verificar que exista el archivo `modelo_backup.pkl`.
3. Confirmar que el procedimiento de rollback es necesario.

---

## Acciones

1. Ejecutar:

```bash
python rollback_model.py
```

2. Verificar el mensaje:

```text
ROLLBACK EJECUTADO CORRECTAMENTE
modelo.pkl fue restaurado desde modelo_backup.pkl
```

3. Ejecutar nuevas predicciones con FastAPI.

4. Confirmar que el servicio continúa operando correctamente.

---

## Resultado esperado

- El archivo `modelo.pkl` corresponde nuevamente a la versión estable.
- Las predicciones vuelven a comportarse de manera normal.
- El servicio permanece disponible.

---

## Evidencia

- Ejecución de `rollback_model.py`.
- Captura de la consola.
- Validación de nuevas predicciones.