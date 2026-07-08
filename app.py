
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

modelo = joblib.load("modelo.pkl")

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

    return {
        "probabilidad_falla": round(float(probabilidad), 4),
        "umbral": umbral,
        "prediccion": prediccion,
        "resultado": resultado
    }
