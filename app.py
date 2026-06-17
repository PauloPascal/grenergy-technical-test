from fastapi import FastAPI, Header, HTTPException
import requests

app = FastAPI()

# Constantes de conexión al CEN
API_KEY_CEN_COSTO = "9c7e337ac19d47ce632bf66d709b2afc"
API_KEY_CEN_MEDIDAS = "6ef7142eebd5105c424274173e91b07e"
# Token interno para securizar tu API propia
MI_TOKEN_SEGURIDAD = "GRENERGY_SECRET_2026"

def get_headers(api_key):
    return {"x-api-key": api_key, "Accept": "application/json", "User-Agent": "GrenergyApp/1.0"}

@app.get("/costo-marginal")
def get_costo(x_api_key: str = Header(...)):
    if x_api_key != MI_TOKEN_SEGURIDAD:
        raise HTTPException(status_code=403, detail="Token interno inválido")
    
    url = "https://sipub.api.coordinador.cl/costo-marginal-online/v4/findByDate"
    params = {"fecha": "2026-06-17", "nodeId": "FRONTERA______220"}
    
    try:
        response = requests.get(url, headers=get_headers(API_KEY_CEN_COSTO), params=params, timeout=10)
        return response.json() if response.status_code == 200 else {"error": f"Error {response.status_code}", "detalle": response.text}
    except Exception as e:
        return {"error": "Error de conexión", "detalle": str(e)}

@app.get("/medidas")
def get_medidas(x_api_key: str = Header(...)):
    if x_api_key != MI_TOKEN_SEGURIDAD:
        raise HTTPException(status_code=403, detail="Token interno inválido")
    
    url = "https://medidas.api.coordinador.cl/medidas-v2/measurement"
    params = {"measurePointId": "FRONTERA_220_J7-J8_QUI"}
    
    try:
        response = requests.get(url, headers=get_headers(API_KEY_CEN_MEDIDAS), params=params, timeout=10)
        return response.json() if response.status_code == 200 else {"error": f"Error {response.status_code}", "detalle": response.text}
    except Exception as e:
        return {"error": "Error de conexión", "detalle": str(e)}