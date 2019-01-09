import datetime, decimal


def alchemy_encoder(obj):
    """
    Enconder de objetos para o formato JSON para tratar casos de tipos especiais de dados. Esta função é comum
    a todos os controllers.

    :param obj: objeto a ser encondificado.
    :return: objeto codificado pronto para dump.
    """
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
