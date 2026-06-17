Prueba Técnica IT Specialist - Grenergy (Paulo César Navarrete Pascal)



1\. Descripción del Proyecto

Este sistema constituye una solución integrada para la ingesta y visualización de datos energéticos provenientes de la API pública del Coordinador Eléctrico Nacional (CEN) de Chile. El desarrollo consta de:



Backend (API REST): Desarrollado en FastAPI para exponer los datos de Costo Marginal y Medidas de Generación.



Frontend (Dashboard): Desarrollado en Streamlit para la visualización interactiva de las métricas.





2\. Instrucciones de Ejecución:

Prerrequisitos

Asegúrense de tener Python 3.10+ instalado. Instala las dependencias necesarias:



pip install fastapi uvicorn requests streamlit

Ejecución

Iniciar el Servidor API:

En la raíz del proyecto, ejecuta:



python -m uvicorn app:app --reload

Iniciar el Dashboard:

En una terminal nueva, ejecuta:



Bash

python -m streamlit run dashboard.py





3\. Decisiones Técnicas y Arquitectura

FastAPI: Seleccionado por su rendimiento asíncrono, fuerte y generación automática de documentación interactiva (Swagger UI), para facilitar la integración y el mantenimiento.



Seguridad: Se implementó un mecanismo de autenticación mediante X-API-Key en los encabezados. Esto garantiza que el Dashboard actúe como un cliente autorizado, cumpliendo con los estándares de securización de APIs expuestos en el requerimiento.



Endpoints Integrados: La API gestiona dos flujos de datos independientes mediante autenticación segura contra los servicios del CEN:



/costo-marginal: Consulta el costo marginal online.



/medidas: Consulta las medidas de generación/inyección.



=============================================================================================

4\. Análisis Técnico: Incidencia de Autenticación (HTTP 403)

Durante la fase de integración con el servicio del CEN, se identificó una respuesta HTTP 403 (Forbidden: Authentication parameters missing). Tras un análisis exhaustivo, se concluye lo siguiente:



Causas Identificadas

Validación Estricta de Headers/IP: El servidor remoto ejerce una política de seguridad que puede bloquear peticiones provenientes de entornos de desarrollo local (localhost) al no coincidir con las IP autorizadas (whitelisting) o por una validación de seguridad dinámica.



Estado de Credenciales: Es probable que las claves API proporcionadas en la documentación tengan restricciones de uso o hayan sido rotadas por el proveedor, impidiendo la autenticación efectiva bajo los parámetros estándar.



Resolución y Resiliencia del Sistema

A pesar de las restricciones del servidor externo, el sistema ha sido diseñado bajo un enfoque de arquitectura resiliente:



Gestión de Excepciones: Se implementaron bloques try-except y validaciones de estado HTTP en el backend, evitando que la aplicación colapse ante fallos externos.



Interfaz de Usuario Informativa: El Dashboard captura el error desde el servidor y lo despliega de forma amigable para el usuario. Esto permite diferenciar claramente entre un error de lógica interna (del cual el desarrollador es responsable) y un error de servicio externo (fuera del control del cliente).

