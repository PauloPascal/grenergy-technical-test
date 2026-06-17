import streamlit as st
import requests

st.title("Grenergy IT Dashboard")

if st.button("Cargar Datos de Quillagua"):
    url_api = "http://127.0.0.1:8000/costo-marginal"
    headers = {"x-api-key": "GRENERGY_SECRET_2026"}
    
    try:
        response = requests.get(url_api, headers=headers, timeout=15)
        if response.status_code == 200:
            datos = response.json()
            if "error" in datos:
                st.error(f"Error: {datos['detalle']}")
            else:
                st.success("Datos recibidos:")
                st.write(datos)
        else:
            st.error(f"Error de conexión: {response.status_code}")
    except Exception as e:
        st.error(f"Error crítico: {e}")