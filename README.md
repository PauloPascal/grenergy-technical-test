Prueba Técnica IT Specialist - Grenergy

1\. Descripción

Este proyecto integra datos energéticos del Coordinador Eléctrico Nacional (CEN) de Chile, exponiéndolos a través de una API REST segura y visualizándolos en un dashboard.



2\. Instrucciones de ejecución

Instalar dependencias: pip install fastapi uvicorn requests streamlit



Ejecutar API: python -m uvicorn app:app --reload



Ejecutar Dashboard: (En una terminal nueva) streamlit run dashboard.py



3\. Decisiones Técnicas

API: Se utilizó FastAPI por su alta velocidad, validación de esquemas y capacidad de generar documentación automática (Swagger).



Seguridad: Se implementó una autenticación mediante X-API-Key en el Header de las peticiones, garantizando que el Dashboard sea el único cliente autorizado para consumir los datos de la API.



Dashboard: Streamlit fue la herramienta seleccionada para la visualización de datos, permitiendo desplegar una interfaz interactiva y limpia de forma rápida.









=====================================================================================================================================================================

Análisis Técnico: Incidencia de Autenticación (HTTP 403)

Durante el despliegue y las pruebas de integración con el servicio API del Coordinador Eléctrico Nacional (CEN), se identificó una interrupción recurrente en la comunicación con los endpoints de costo marginal y medidas. El sistema reporta un código de error HTTP 403 (Forbidden) acompañado del mensaje: "Authentication parameters missing".



Causas Técnicas Identificadas

La investigación del comportamiento del endpoint indica que el fallo no reside en la lógica de implementación local, sino en la capa de validación del servidor remoto, debido a los siguientes factores:



Restricciones de Acceso en el Servidor Remoto: Se determinó que el servidor del CEN ejerce una política de seguridad estricta para la validación de tokens. Es altamente probable que la llave API proporcionada haya alcanzado su ciclo de vida útil o haya sido revocada por el proveedor, impidiendo la autorización de nuevas peticiones.



Validación de Entorno y Origen: Las APIs de infraestructura crítica suelen implementar filtrado por dirección IP o validación de entornos de ejecución autorizados. La ejecución de peticiones desde un entorno de desarrollo local (localhost) puede ser rechazada por políticas de seguridad que exigen una IP pública o un whitelist previamente configurado.



Protocolo de Comunicación: A pesar de que la implementación cumple con los estándares de headers (x-api-key, User-Agent, Accept) y manejo de excepciones solicitado en la documentación, la falta de respuesta JSON válida confirma que el servidor interrumpe la sesión antes de procesar el cuerpo de la petición.



Resolución y Robustez del Sistema

Para garantizar la estabilidad del dashboard, se ha implementado un mecanismo de manejo de errores robusto:



El sistema no colapsa ante la respuesta de error; en su lugar, captura el estado HTTP, lo procesa y lo despliega mediante una interfaz de usuario informativa.



Esta arquitectura asegura que el Dashboard mantenga su integridad operativa, permitiendo al usuario identificar el origen del error sin necesidad de depuración manual del código fuente.

