
from flask_app.config.mysqlconnection import connectToMySQL


class Curso:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO cursos (nombre, created_at, updated_at)
            VALUES (%(nombre)s, NOW(), NOW());
        """
        return connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos ORDER BY id ASC;"
        resultados = connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query)

        return [cls(fila) for fila in resultados] if resultados else []

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        resultados = connectToMySQL(
            "esquema_estudiantes_cursos"
        ).query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None
