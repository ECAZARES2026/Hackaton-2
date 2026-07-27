
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import time
from datetime import datetime
from pathlib import Path
import uuid


app = FastAPI()

modelo = joblib.load("modelo.pkl")
LOG_FILE = Path("monitoring_logs.csv")

COLUMNAS_LOG = [
    "trace_id",
    "timestamp",
    "Type",
    "Air_temperature_K",
    "Process_temperature_K",
    "Rotational_speed_rpm",
    "Torque_Nm",
    "Tool_wear_min",
    "probabilidad_falla",
    "umbral",
    "prediccion",
    "resultado",
    "latencia_ms",
    "estado"
]   

class DatosEntrada(BaseModel):
    Type: int
    Air_temperature_K: float
    Process_temperature_K: float
    Rotational_speed_rpm: float
    Torque_Nm: float
    Tool_wear_min: int

@app.get("/")
def home():
    return {"mensaje": "API mexa de predicción de fallas CDU activa 🇲🇽🤖"}

@app.post("/predict")
def predict(datos: DatosEntrada):
    inicio = time.perf_counter()
    trace_id = str(uuid.uuid4())


    entrada = pd.DataFrame([{
        "Type": datos.Type,
        "Air temperature K": datos.Air_temperature_K,
        "Process temperature K": datos.Process_temperature_K,
        "Rotational speed rpm": datos.Rotational_speed_rpm,
        "Torque Nm": datos.Torque_Nm,
        "Tool wear min": datos.Tool_wear_min
    }])

    probabilidad = modelo.predict_proba(entrada)[0][1]
    umbral = 0.30
    prediccion = int(probabilidad >= umbral)

    resultado = "Riesgo de falla" if prediccion == 1 else "Sin falla esperada"

    latencia_ms = (time.perf_counter() - inicio) * 1000

    registro = pd.DataFrame([{
    "trace_id": trace_id,
    "timestamp": datetime.now().isoformat(timespec="seconds"),
    "Type": datos.Type,
    "Air_temperature_K": datos.Air_temperature_K,
    "Process_temperature_K": datos.Process_temperature_K,
    "Rotational_speed_rpm": datos.Rotational_speed_rpm,
    "Torque_Nm": datos.Torque_Nm,
    "Tool_wear_min": datos.Tool_wear_min,
    "probabilidad_falla": round(float(probabilidad), 4),
    "umbral": umbral,
    "prediccion": prediccion,
    "resultado": resultado,
    "latencia_ms": latencia_ms,
    "estado": "OK" 
    }])

    registro.to_csv(LOG_FILE, mode="a", header=not LOG_FILE.exists(), index=False)

    return {
        "trace_id": trace_id,
        "probabilidad_falla": round(float(probabilidad), 4),
        "umbral": umbral,
        "prediccion": prediccion,
        "resultado": resultado,
        "latencia_ms": round(latencia_ms, 4),
    }
