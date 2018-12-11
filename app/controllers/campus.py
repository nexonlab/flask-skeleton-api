from ..errors import ErroInterno, TipoErro
from ..dao import campus as campus_dao


def recuperar_campus():
    """
    Recupera uma lista de campus.

    :return: uma lista de objetos contendo informacoes dos campi.
    :exception ErroInterno
    """
    try:
        result = campus_dao.recupera_campus()
        resposta = []
        for id_campus, descricao in result:
            resposta.append({"id": id_campus, "descricao": str(descricao).strip()})

        return resposta
    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar Campi disponíveis.")
