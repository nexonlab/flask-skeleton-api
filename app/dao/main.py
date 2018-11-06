from ..models.db import db


def main_dao_function():
    """Main DAO Function"""
    return "Hello World"


# This is an example, remove this when building your project
def recupera_campus():
    """
    Busca os campus a partir do codigo da turma e retorna uma lista de objetos com as informacoes dos campus.

    :return: uma lista com todos os campus para a qual aquela turma esta aberta.
    :exception Exception: Lança uma exceção genérica caso ocorra algum erro.
    """
    try:
        sql = db.select([
            db.text("EXB5CODCAM, EXB5DESCAM")
        ]).select_from(
            db.text("EXB5CAMPUT WITH (NOLOCK)")
        )

        resultado = db.engine.execute(sql).fetchall()

        return resultado
    except Exception as e:
        raise e
