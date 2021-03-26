from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def entry():
    students = getStudents()
    return render_template("viewer-panel.html", students=students)


def getStudents():
    return [ "Jaimito", "Jorgito", "Juanito" ]