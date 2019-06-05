import logging
from flask import Flask, request, current_app
from datetime import datetime
from logging import StreamHandler
from flask_cors import CORS
from .models.db import db
from .config import DevelopmentConfig


__author__ = "{{cookiecutter.author}}"
__email__ = "{{cookiecutter.email}}"
__version__ = "{{cookiecutter.version}}"


def log_request():
    try:
        # caso mude o WSGI, entao isso aqui devera mudar tambem
        logger = logging.getLogger('waitress')
        logger.setLevel(logging.INFO)
        logger.info("\t{asctime} \t {level} \t {ip} \t {method} \t {url}".format(asctime=datetime.now().
                                                                                 strftime("%d-%m-%Y %H:%M:%S"),
                                                                                 level="INFO",
                                                                                 ip=request.remote_addr,
                                                                                 method=str(request.method),
                                                                                 url=request.path))
    except Exception as e:
        current_app.logger.error(e)


def create_app(test_config=None):

    # cria e configura a aplicacao
    app = Flask(__name__, instance_relative_config=True)

    # configura log da aplicacao
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = StreamHandler()
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # modificando prefixo da url
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/{{cookiecutter.app_name}}')

    if test_config is None:
        # carrega uma instancia de configuracao
        app.config.from_object(DevelopmentConfig)
    else:
        # carrega a instancia test_config passada por parametro
        app.config.from_mapping(test_config)

    # registra as blueprints de resources
    from .resources.campus import bp as bp_campus
    from .resources.aluno import bp as bp_aluno
    from .resources.docs import bp as bp_docs
    app.register_blueprint(bp_campus)
    app.register_blueprint(bp_aluno)
    app.register_blueprint(bp_docs)

    db.init_app(app)
    CORS(app)

    # registrando log antes da requisicao
    app.before_request(log_request)

    return app


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["Esta URL nao pertence a aplicacao. Por favor, insira o prefixo '/{{cookiecutter.app_name}}'."
                    .encode()]
