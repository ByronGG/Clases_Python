"""
    ¿Qué es Flask?

    Flask es un microframework web escrito en Python. "Micro" no significa que le falten funcionalidades importantes — significa que el núcleo es minimalista y no te impone estructura, base de datos, ni herramientas específicas. Tú decides qué agregar.

    Fue creado por Armin Ronacher en 2010, y se basa en dos librerías:

    - Werkzeug: el motor WSGI que maneja las peticiones/respuestas HTTP a bajo nivel.
    - Jinja2: el motor de plantillas (templates) para generar HTML dinámico.
    
    ¿Para qué sirve?
    * APIs REST (como las que ya haces con FastAPI, pero en un estilo más manual)
    * Aplicaciones web tradicionales con HTML renderizado en el servidor
    * Prototipos rápidos y MVPs
    * Microservicios pequeños
    * Backends para dashboards internos
"""
# ======================================================================
"""
Instalación
Se recomienda que cualquier proyecto Python se use un entorno virtual
    1. Crear entorno virtual
    python -m venv venv
    2. Activarlo (Linux/Mac)
    source venv/bin/activate
    3. Activar Windows
    venv\Scripts\activate
    4. Instalar Flask
    pip install flask

    Para revisar si esta instalado usar el siguiente comando en terminal (dentro del venv)
    python -c "import flask; print(flask.__version__)"
"""
# ======================================================================
"""
Para crear la primar APP
Crear un archivo llmado 'app.py' (Root)

from flask import Flask

app = Flask(__name__)@

@app.route("/")
def home():
    return "Hola desde Flask!"

if __name__ == "__main__":
    app.run(debug=True)

Esto levanta un servidor en http://127.0.0.1:5000/. El parámetro debug=True activa recarga automática y un debugger interactivo en el navegador si algo falla — nunca en producción, es un riesgo de seguridad grave (permite ejecutar código arbitrario si alguien accede al debugger).

Estructura MÍNIMA de un proyecto
Para algo pequeño, un solo archivo basta. Pero confome creece, una estructura típica es:

mi_proyecto/
├── venv/
├── app.py              # o run.py
├── requirements.txt
├── static/              # CSS, JS, imágenes
│   └── style.css
├── templates/            # archivos HTML (Jinja2)
│   └── index.html
└── .env

Flask busca automátricmanet las carpetas static/ y templates/ por convecnión - no necesitas configurarlas
"""
# ======================================================================
"""

"""