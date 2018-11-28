from ..errors import ErroInterno, TipoErro
from ..dao.main import mock_dao_function_array, mock_dao_function_database


def main_function():
    """Main Function"""
    try:
        array_data = mock_dao_function_array()
        result = []

        for (k, v) in array_data.items():
            result.append({
                k: {
                    'id': v['id'],
                    'name': v['name'],
                    'email': v['email'],
                    'age': v['age'],
                    'active': v['active'],
                    'updated_at': v['updated_at']
                }
            })

            return result
    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar Campi disponíveis.")


def recuperar_campus():
    """
    Description Function

    :return: type
    :exception Exception: description Exception Type
    """
    try:
        array_data = mock_dao_function_database()
        result = []
        for field_1, field_2 in array_data:
            result.append({"field_1": field_1, "field_2": str(field_2).strip()})

        return result
    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar Campi disponíveis.")
