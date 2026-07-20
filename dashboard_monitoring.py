import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Dashboard de Monitorización",
    layout="wide"
)

st.title("Dashboard de Monitorización de Predicción de fallas con IA")

LOG_FILE = Path("monitoring_logs.csv")

if not LOG_FILE.exists():
    st.error("No se encontró el archivo monitoring_logs.csv")
    st.stop()

df = pd.read_csv(LOG_FILE)

if df.empty:
    st.warning("El archivo de monitoreo no contiene registros.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

total_predicciones = len(df)
latencia_promedio = df["latencia_ms"].mean()
latencia_maxima = df["latencia_ms"].max()
riesgos_detectados = int(df["prediccion"].sum())
probabilidad_promedio = df["probabilidad_falla"].mean()

LATENCIA_WARNING_MS = 500
LATENCIA_CRITICAL_MS = 1000

if latencia_maxima > LATENCIA_CRITICAL_MS:
    estado_servicio = "CRÍTICO"
elif latencia_maxima > LATENCIA_WARNING_MS:
    estado_servicio = "ADVERTENCIA"
else:
    estado_servicio = "NORMAL"

st.subheader("Indicadores operativos")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Predicciones", total_predicciones)
col2.metric("Latencia promedio", f"{latencia_promedio:.2f} ms")
col3.metric("Latencia máxima", f"{latencia_maxima:.2f} ms")
col4.metric("Riesgos detectados", riesgos_detectados)
col5.metric("Estado del servicio", estado_servicio)

st.divider()

st.subheader("Latencia del servicio")

grafica_latencia = df[["timestamp", "latencia_ms"]].dropna()
grafica_latencia = grafica_latencia.set_index("timestamp")

st.line_chart(grafica_latencia)

st.subheader("Probabilidad de falla")

grafica_probabilidad = df[
    ["timestamp", "probabilidad_falla"]
].dropna()

grafica_probabilidad = grafica_probabilidad.set_index("timestamp")

st.line_chart(grafica_probabilidad)

st.subheader("Distribución de resultados")

distribucion = (
    df["resultado"]
    .value_counts()
    .rename_axis("resultado")
    .reset_index(name="cantidad")
)

st.bar_chart(distribucion, x="resultado", y="cantidad")

st.subheader("Alertas activas")

alertas = []

if latencia_maxima > LATENCIA_CRITICAL_MS:
    alertas.append(
        f"CRÍTICA: latencia máxima de {latencia_maxima:.2f} ms."
    )
elif latencia_maxima > LATENCIA_WARNING_MS:
    alertas.append(
        f"ADVERTENCIA: latencia máxima de {latencia_maxima:.2f} ms."
    )

if probabilidad_promedio > 0.50:
    alertas.append(
        f"ADVERTENCIA: probabilidad promedio de falla "
        f"{probabilidad_promedio:.2%}."
    )

if riesgos_detectados > 0:
    alertas.append(
        f"Se detectaron {riesgos_detectados} predicciones con riesgo."
    )

if alertas:
    for alerta in alertas:
        st.warning(alerta)
else:
    st.success("No existen alertas operativas activas.")

st.divider()

st.subheader("Histórico de predicciones")

st.dataframe(
    df.sort_values("timestamp", ascending=False),
    use_container_width=True
)