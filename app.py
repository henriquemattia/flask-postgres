from flask import Flask
from database import cursor
from database import connection


app = Flask(__name__)

# @app.route("/users")
# def list_all():
#     cursor.execute("SELECT *FROM aluno")
#     lista_alunos = cursor.fetchall()
#     primeiro_aluno = lista_alunos[0]
#
#     return {"id": primeiro_aluno, "nome": primeiro_aluno[1]}, 200


@app.route("/users/<user_id>", methods=["PUT"])
def update(user_id):
    cursor.execute(f"UPDATE aluno SET nome = 'Douglas' WHERE id = {user_id}")
    connection.commit()
    return user_id