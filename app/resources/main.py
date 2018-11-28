import simplejson
from flask import (make_response, Blueprint, jsonify)
from ..controllers.main import main_function
from ..errors import ErroInterno, UsoInvalido


bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/', methods=('GET',))
def get_campus():
    try:
        resposta = main_function()

        response = make_response(simplejson.dumps(resposta, ensure_ascii=False), 200)
        response.headers['Content-Type'] = 'application/json'

        return response
    except UsoInvalido as e:
        raise e
    except ErroInterno as e:
        raise e
    except Exception as e:
        raise e


@bp.errorhandler(UsoInvalido)
def not_found(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@bp.errorhandler(ErroInterno)
def internal_server_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
