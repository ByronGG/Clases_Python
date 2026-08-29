from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "cambiar_esto_por_algo_seguro" # requerido para flash y sesiones

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = request.form.get("edad", "").strip()

        # Validación manual
        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        if not edad.isdigit():
            errores.append("La edad debe ser un número.")
        elif int(edad) < 18:
            errores.append("Debes ser mayor de edad.")

        if errores:
            for e in errores:
                flash(e, "error")
            # Re-renderizamos conservando lo que ya escribió
            return render_template("registro.html", datos=request.form)

        flash(f"Registro existoso: {nombre}, {edad} años.", "exito")
        return redirect(url_for("registro")) #<- el Redirect del patron PRG
    return render_template("registro.html", datos={})