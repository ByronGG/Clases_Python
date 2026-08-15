from flask import Flask, render_template

app = Flask(__name__)

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return render_template("index.html", nombre=nombre, edad=20)

if __name__ == "__main__": # Constructor de python que llama a main
    app.run(debug=True) # Ejecuta la entrada de Flask (app) y lo pone en debug Verdadero para no romper producción