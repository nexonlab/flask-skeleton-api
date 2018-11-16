from ..errors import ErroInterno, TipoErro
from ..dao import main as main_dao


def main_function():
    """Main Function"""
    return main_dao.main_dao_function()


def recuperar_campus():
    """
    Recupera uma lista de campus com id e descricao a partir do codigo da turma.

    :return: uma lista de dicionarios com ID e DESCRICAO de cada Campus.
    :exception ErroInterno
    """
    try:
        result = main_dao.recupera_campus()
        resposta = []
        for id_campus, descricao in result:
            resposta.append({"id": id_campus, "descricao": str(descricao).strip()})

        return resposta
    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar Campi disponíveis.")
