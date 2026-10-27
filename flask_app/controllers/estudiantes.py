
from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso


@app.route("/estudiante")
def nuevo_estudiante():
    cursos = Curso.get_all()

    return render_template(
        "add_estudiante_curso.html",
        cursos=cursos
    )


@app.route("/estudiante/crear", methods=["POST"])
def crear_estudiante():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    cursos_id = request.form.get("cursos_id", "").strip()

    if not nombre or not apellido or not edad or not cursos_id:
        return redirect(url_for("nuevo_estudiante"))

    try:
        edad = int(edad)
        cursos_id = int(cursos_id)
    except ValueError:
        return redirect(url_for("nuevo_estudiante"))

    if edad < 1:
        return redirect(url_for("nuevo_estudiante"))

    # Comprobar que el curso seleccionado exista
    curso = Curso.get_by_id({"id": cursos_id})

    if curso is None:
        return redirect(url_for("nuevo_estudiante"))

    data = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cursos_id": cursos_id
    }

    Estudiante.save(data)

    return redirect(url_for("vista_curso", curso_id=cursos_id))
