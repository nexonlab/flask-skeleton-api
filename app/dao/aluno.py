from ..models.db import db


def recupera_aluno(cpd=None):
    try:
        sql = db.select([
            db.text("CPD, NOME")
        ]).select_from(
            db.text("ALUNO")
        )

        if cpd is not None:
            sql = sql.where(db.text("CPD = :cpd"))
            resultado = db.engine.execute(sql, cpd=cpd).fetchall()
        else:
            resultado = db.engine.execute(sql).fetchall()

        return resultado
    except Exception as e:
        raise e
