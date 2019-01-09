from ..models.db import db


def recupera_campus():
    """
    Busca todos os campi disponíveis.

    :return: uma lista com todos os campi.
    :exception Exception: Lança uma exceção genérica caso ocorra algum erro.
    """
    try:
        sql = db.select([
            db.text("CODIGO, DESCRICAO")
        ]).select_from(
            db.text("CAMPUS")
        )

        resultado = db.engine.execute(sql).fetchall()

        return resultado
    except Exception as e:
        raise e
