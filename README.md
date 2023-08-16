FastAPI App para el Segundo Reto de la Prueba Técnica

Este es el README para la aplicación de FastAPI que sirve como backend para el segundo reto de la prueba técnica. Esta aplicación proporciona una API para gestionar y manipular datos relacionados con préstamos de equipos.

Entorno Virtual
Se recomienda utilizar un entorno virtual para aislar las dependencias de este proyecto de otros proyectos Python en tu sistema. Sigue estos pasos para configurar el entorno virtual:

Abre una terminal en la ubicación donde clonaste este repositorio.

Crea un nuevo entorno virtual:

bash
Copy code
python -m venv venv
Activa el entorno virtual:

En Windows:
bash
Copy code
venv\Scripts\activate
En macOS y Linux:
bash
Copy code
source venv/bin/activate
Montar una API en FastAPI
Sigue estos pasos para ejecutar la aplicación FastAPI y montar una API para gestionar los préstamos de equipos:

Asegúrate de que el entorno virtual esté activado.

Instala las dependencias usando pip:

bash
Copy code
pip install -r requirements.txt
Ejecuta la aplicación con el siguiente comando:

bash
Copy code
uvicorn app.main:app --host 0.0.0.0 --port 8000
La aplicación estará disponible en http://localhost:8000.

Accede a la documentación interactiva de la API generada automáticamente por FastAPI en http://localhost:8000/docs. Aquí encontrarás los endpoints disponibles y podrás probarlos directamente desde el navegador.

Datos Personales
Nombre: Jair Santiago Leal Miranda
Documento: 1000293157
Nota sobre la Base de Datos
La base de datos para esta aplicación está en la nube y no requiere ninguna configuración adicional. La conexión a la base de datos ya está preconfigurada para funcionar sin modificaciones.