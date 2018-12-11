import simplejson
from flask import (make_response, Blueprint, current_app)
from ..controllers import campus as main_controller
from ..errors import ErroInterno, UsoInvalido, TipoErro
from . import generic_handler


bp = Blueprint('campus', __name__, url_prefix='/campus')
bp.register_error_handler(ErroInterno, generic_handler)
bp.register_error_handler(UsoInvalido, generic_handler)


@bp.route('/', methods=('GET',))
def get_campus():
    try:
        resposta = main_controller.recuperar_campus()

        response = make_response(simplejson.dumps(resposta, ensure_ascii=False), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    except UsoInvalido as e:
        current_app.logger.error(e)
        raise e
    except ErroInterno as e:
        current_app.logger.error(e)
        raise e
    except Exception as e:
        current_app.logger.error(e)
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar campi.")
