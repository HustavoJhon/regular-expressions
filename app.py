from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Expresión regular 
REGEX = r"^h(?:(agh|ftsh|ouh)){3,}x$"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    cadena = ""
    if request.method == "POST":
        cadena = request.form.get("cadena", "").strip()
        if re.fullmatch(REGEX, cadena):
            result = "Cadena ACEPTADA."
        else:
            result = "Cadena RECHAZADA."
    return render_template("index.html", result=result, regex=REGEX, cadena=cadena)

if __name__ == "__main__":
    app.run(debug=True)

