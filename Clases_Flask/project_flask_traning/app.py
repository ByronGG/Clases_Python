from flask import Flask # Importamos microframework

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

if __name__ == "__main__": # Constructor de python que llama a main
    app.run(debug=True) # Ejecuta la entrada de Flask (app) y lo pone en debug Verdadero para no romper producción