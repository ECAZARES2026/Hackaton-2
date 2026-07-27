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

if "trace_id" not in df.columns:
    df["trace_id"] = "registro_historico"

if df.empty:
    st.warning("El archivo de monitoreo no contiene registros.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

total_predicciones = len(df)
latencia_promedio = df["latencia_ms"].mean()
latencia_maxima = df["latencia_ms"].max()
riesgos_detectados = int(df["prediccion"].sum())
probabilidad_promedio = df["probabilidad_falla"].mean()

# ==============================
# SLO - Service Level Objective
# ==============================

SLO_LATENCIA_MS = 500

predicciones_en_slo = len(
    df[df["latencia_ms"] <= SLO_LATENCIA_MS]
)

porcentaje_slo = (
    predicciones_en_slo / total_predicciones
) * 100

# ==============================
# Error Budget
# ==============================

SLO_OBJETIVO = 99.0

# Presupuesto total permitido de incumplimiento
error_budget = 100 - SLO_OBJETIVO

# Porcentaje real de solicitudes fuera del SLO
error_real = 100 - porcentaje_slo

if error_real <= error_budget:
    estado_slo = "✅ Cumplido"
else:
    estado_slo = "❌ No cumplido"

LATENCIA_WARNING_MS = 500
LATENCIA_CRITICAL_MS = 1000

if latencia_maxima > LATENCIA_CRITICAL_MS:
    estado_servicio = "CRÍTICO"
elif latencia_maxima > LATENCIA_WARNING_MS:
    estado_servicio = "ADVERTENCIA"
else:
    estado_servicio = "NORMAL"

st.subheader("Indicadores operativos")

# ==============================
# Indicadores Operativos
# ==============================

fila1_col1, fila1_col2, fila1_col3, fila1_col4 = st.columns(4)

fila1_col1.metric(
    "Predicciones",
    total_predicciones
)

fila1_col2.metric(
    "Latencia promedio",
    f"{latencia_promedio:.2f} ms"
)

fila1_col3.metric(
    "Latencia máxima",
    f"{latencia_maxima:.2f} ms"
)

fila1_col4.metric(
    "Estado del servicio",
    estado_servicio
)

# ==============================
# Indicadores de Confiabilidad
# ==============================

fila2_col1, fila2_col2, fila2_col3, fila2_col4 = st.columns(4)

fila2_col1.metric(
    "Riesgos detectados",
    riesgos_detectados
)

fila2_col2.metric(
    "Cumplimiento SLO",
    f"{porcentaje_slo:.1f}%"
)

fila2_col3.metric(
    "Error real",
    f"{error_real:.1f}%"
)

fila2_col4.metric(
    "Estado del SLO",
    estado_slo
)
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

ultimo_trace = df.iloc[-1]["trace_id"]

if latencia_maxima > LATENCIA_CRITICAL_MS:
   alertas.append(
    f"""CRÍTICA

Trace ID: {ultimo_trace}

Latencia máxima: {latencia_maxima:.2f} ms

Acción:
Ejecutar Runbook RB-001."""
)
elif latencia_maxima > LATENCIA_WARNING_MS:
    alertas.append(
    f"""ADVERTENCIA

Trace ID: {ultimo_trace}

Latencia máxima: {latencia_maxima:.2f} ms

Acción:
Revisar comportamiento de la API."""
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
st.subheader("🔎 Buscar solicitud por Trace ID")

trace_buscado = st.text_input(
    "Ingrese el Trace ID:"
).strip()

if trace_buscado:
    resultado = df[
        df["trace_id"].astype(str).str.contains(
            trace_buscado,
            case=False,
            na=False
        )
    ]

    if resultado.empty:
        st.warning("No se encontró ese Trace ID.")
    else:
        st.success("Solicitud localizada.")
        st.dataframe(
            resultado,
            use_container_width=True
        )

st.divider()
st.subheader("Histórico de predicciones")

st.dataframe(
    df.sort_values("timestamp", ascending=False),
    use_container_width=True
)