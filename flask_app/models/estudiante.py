
from flask_app.config.mysqlconnection import connectToMySQL


class Estudiante:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.cursos_id = data["cursos_id"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO estudiantes
            (nombre, apellido, edad, cursos_id, created_at, updated_at)
            VALUES
            (%(nombre)s, %(apellido)s, %(edad)s, %(cursos_id)s,
             NOW(), NOW());
        """
        return connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

    @classmethod
    def get_all_by_curso(cls, data):
        query = """
            SELECT *
            FROM estudiantes
            WHERE cursos_id = %(cursos_id)s
            ORDER BY apellido ASC;
        """
        resultados = connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

        return [cls(fila) for fila in resultados] if resultados else []
