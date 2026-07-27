from pathlib import Path

import pandas as pd


LOG_FILE = Path("monitoring_logs.csv")

COLUMNAS_MONITOREADAS = [
    "Air_temperature_K",
    "Process_temperature_K",
    "Rotational_speed_rpm",
    "Torque_Nm",
    "Tool_wear_min",
]

UMBRAL_VARIACION = 0.30


def detectar_data_drift() -> tuple[bool, pd.DataFrame]:
    if not LOG_FILE.exists():
        raise FileNotFoundError("No se encontró monitoring_logs.csv")

    df = pd.read_csv(LOG_FILE)

    if len(df) < 4:
        raise ValueError("Se requieren al menos 4 registros para evaluar drift.")

    mitad = len(df) // 2

    referencia = df.iloc[:mitad]
    datos_recientes = df.iloc[mitad:]

    resultados = []

    for columna in COLUMNAS_MONITOREADAS:
        promedio_referencia = referencia[columna].mean()
        promedio_reciente = datos_recientes[columna].mean()

        if promedio_referencia == 0:
            variacion = 0.0
        else:
            variacion = abs(
                promedio_reciente - promedio_referencia
            ) / abs(promedio_referencia)

        drift_detectado = variacion > UMBRAL_VARIACION

        resultados.append(
            {
                "variable": columna,
                "promedio_referencia": promedio_referencia,
                "promedio_reciente": promedio_reciente,
                "variacion_pct": variacion * 100,
                "drift_detectado": drift_detectado,
            }
        )

    detalle = pd.DataFrame(resultados)
    drift_general = bool(detalle["drift_detectado"].any())

    return drift_general, detalle

if __name__ == "__main__":
    drift, detalle = detectar_data_drift()

    print("\nEstado general:")
    print("DATA DRIFT DETECTADO" if drift else "SIN DATA DRIFT")

    print("\nDetalle:")
    print(detalle.to_string(index=False))

