import streamlit as st
import requests

st.title("Grenergy IT Dashboard")

if st.button("Cargar Datos de Quillagua"):
    try:
        # Llamada a tu propia API
        response = requests.get("http://127.0.0.1:8000/costo-marginal", headers={"x-api-key": "GRENERGY_SECRET_2026"}, timeout=10)
        datos = response.json()
        
        if "error" in datos:
            st.error(f"Error desde API: {datos.get('error')} - {datos.get('detalle')}")
        else:
            st.success("Datos obtenidos exitosamente:")
            st.json(datos)
    except Exception as e:
        st.error(f"Error crítico de conexión: {str(e)}")