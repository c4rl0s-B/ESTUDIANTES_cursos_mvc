
from flask_app import app
from flask import flash, render_template, redirect, request, url_for
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route('/')
def inicio():
    return redirect('/cursos')

@app.route("/cursos")
def cursos():
    lista_cursos = Curso.get_all()
    return render_template("cursos.html", cursos=lista_cursos)


@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    nombre = request.form.get("nombre", "").strip()

    if not nombre:
        flash("El nombre del curso no puede estar vacío.", "error")
        return redirect(url_for("cursos"))

    Curso.save({"nombre": nombre})
    return redirect(url_for("cursos"))


@app.route("/cursos/<int:curso_id>")
def vista_curso(curso_id):
    curso = Curso.get_by_id({"id": curso_id})

    if curso is None:
        flash("Curso no encontrado.", "error")
        return redirect(url_for("cursos"))

    estudiantes = Estudiante.get_all_by_curso({"cursos_id": curso_id})

    return render_template("vista_cursos.html",curso=curso,estudiantes=estudiantes)
