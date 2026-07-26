# Runbook RB-001
## Alta Latencia del Servicio

### Objetivo

Restablecer el tiempo de respuesta del servicio FastAPI cuando la latencia exceda el límite establecido.

---

## Condición de activación

- Latencia promedio > 500 ms
- Dashboard indica estado de ADVERTENCIA o CRÍTICO.

---

## Diagnóstico

1. Abrir el Dashboard de Monitoreo.
2. Verificar la métrica **Latencia promedio**.
3. Revisar la gráfica histórica de latencia.
4. Confirmar que el problema sea persistente.

---

## Acciones

1. Revisar el consumo de CPU y memoria del servidor.
2. Verificar que FastAPI continúe en ejecución.
3. Revisar el archivo `monitoring_logs.csv`.
4. Reiniciar el servicio FastAPI si la latencia continúa elevada.
5. Ejecutar nuevas predicciones para validar la recuperación.

---

## Resultado esperado

- Latencia promedio menor a 500 ms.
- Estado del servicio = NORMAL.
- El Dashboard vuelve a mostrar métricas dentro del SLO.

---

## Evidencia

- Captura del Dashboard.
- Captura del archivo `monitoring_logs.csv`.
- Captura de la recuperación del servicio.