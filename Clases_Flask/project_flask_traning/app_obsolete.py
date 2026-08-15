from flask import Flask # Importamos microframework
from flask import request

app = Flask(__name__) # metodo de entrada Flask (app)

@app.route("/") # Ruta home o raíz (/) -> si la ruta no es home o necesitas que sea otra se escifica aquí ("/dashboard")
def home(): #home es nombre "normal o comun con el que vamos a llamar la ruta decalrada"
    return "Hola desde Flask!" # Return renderiza el resultado de la ruta -> "Hola desde Flask!" aparece en la pagina web

@app.route("/acerca")
def acerca():
    return "Página de acerda de..."

@app.route("/contacto")
def contacto():
    return "Página de contacto"

# Métodos HTTP: GET -> Obtener | POST -> Publicar | UPDATE -> Actualizar | DELETE -> Borrar | PATCH -> Actulizar 'Parcialmente'
# Método HTTP NUEVO (Al menos propuesto): QUERY -> GET/POST Juntos

@app.route("/enviar", methods=["GET", "POST"]) # Lista de metodos GET y POST
def enviar(): # Método de enviar
    if request.method == "POST": # Condición si yo posteo algo (enviar datos a la app)
        return "Recibido por POST" # Condición si pido algo (obtener datos de la app)
    return "Muestra el formulario (GET)" # GET

# Parámetros en la URL
@app.route("/usuario/<nombre>")
def perfil(nombre):
    return f"Perfil de {nombre}"

@app.route("/productos/<int:id>")
def producto(id):
    return f"Producto número {id}"

# Peticiones (Objetos)
@app.route("/buscar")
def buscar():
    query = request.args.get("q", "")
    return f"Buscando {query}"

@app.route("/formulario", methods=["POST"])
def formulario():
    nombre = request.form.get("nombre")
    return f"Hola {nombre}"

@app.route("/api/datos", methods=["POST"])
def datos():
    body = request.get_json()
    return {"recibido": body}

if __name__ == "__main__": # Constructor de python que llama a main
    app.run(debug=True) # Ejecuta la entrada de Flask (app) y lo pone en debug Verdadero para no romper producción