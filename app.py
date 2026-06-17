from fastapi import FastAPI, Header, HTTPException
import requests

app = FastAPI()

# Constantes
API_KEY_CEN_COSTO = "9c7e337ac19d47ce632bf66d709b2afc"
MI_TOKEN_SEGURIDAD = "GRENERGY_SECRET_2026"

@app.get("/costo-marginal")
def get_costo(x_api_key: str = Header(...)):
    if x_api_key != MI_TOKEN_SEGURIDAD:
        raise HTTPException(status_code=403, detail="Token inválido")
    
    url = "https://sipub.api.coordinador.cl/costo-marginal-online/v4/findByDate"
    # Header estricto para el CEN
    headers = {
        "api-key": API_KEY_CEN_COSTO,
        "Accept": "application/json"
    }
    params = {"fecha": "2026-06-17", "nodeId": "FRONTERA______220"}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        if response.status_code != 200:
            return {"error": "Error del CEN", "detalle": f"HTTP {response.status_code}"}
        return response.json()
    except Exception as e:
        return {"error": "Error de conexión", "detalle": str(e)}