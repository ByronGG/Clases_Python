# Método HTTP
"""
    Una ruta solo responde a GET. Si quieres manejar otros métodos, los especificas explicitamente
    Cada método HTTP en Flask necesita un decorador!! (@app.get, @app.post, @app.patch, ect)

    @app.route("/enviar", methods=["GET", "POST"])
    def enviar():
        for flask import request
        if request.method == "POST":
            return "Recibido por POST"
        return "Muestra el formualario (GET)"

    Parámetros en la URL
    @app.route("/usuario/<nombre>)
    def perfil(nombre):
        return f"Perfil de {nombre}

    @app.route("/producto/<int:id>")
    def producto(id):
        return f"Producto número {id}"
    
    Los converdores disponibles son string (default), int, flout, path, uuid
"""

"""
    Objetos: Todo lo que llega del cliente pasa por 'request'

    from flask import request

    @app.route("/buscar")
    def buscar():
        query = request.args.get("q", "")
        return f"Buscando {query}"
"""

"""
    Templates con Jinja2
    Flask busca archivos HTML en la carpeta templates/.

    mi_proyecto/
    ---app.py
    ---templtes/
    ------index.html
    ---static/
    ------style.css
    ------script.js

    Jinja2 usa {{ }} para imprimir varialbes y {% %} para lógica (if, for, ect). Tambien soporta herencia de plantilasl con {% extends %} y {% block %}, muy útil para no reportir el <head> y navbar en cada página.

    Archivos estáticos
    Todo lo que pongas en static/ (CSS, JS, imágenes) se sirve automaticamente
    <link rel="stylesheet" href="{{ url_for ('static', filename=style.css) }}">

    url_for() genera la URL correcta automáticamnete -evita hardcoodear rutas
"""