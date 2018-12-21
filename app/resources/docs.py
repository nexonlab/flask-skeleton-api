from flask import (make_response, Blueprint, current_app, render_template)
from ..errors import ErroInterno, UsoInvalido, TipoErro
from . import generic_handler


bp = Blueprint('docs', __name__, url_prefix='/apidocs')
bp.register_error_handler(ErroInterno, generic_handler)
bp.register_error_handler(UsoInvalido, generic_handler)


@bp.route('/', methods=('GET',))
def apidocs():
    """
    View function para retornar a documentacao de API.
    """
    try:
        return render_template('/apidocs/index.html')
    except UsoInvalido as e:
        current_app.logger.error(e)
        raise e
    except ErroInterno as e:
        current_app.logger.error(e)
        raise e
    except Exception as e:
        current_app.logger.error(e)
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar campi.")
