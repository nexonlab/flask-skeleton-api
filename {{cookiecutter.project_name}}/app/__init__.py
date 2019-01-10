from flask import Flask
from flask_cors import CORS
from .models.db import db
from .config import DevelopmentConfig
from flasgger import Swagger

import os

__author__ = "{{cookiecutter.author}}"
__email__ = "{{cookiecutter.email}}"
__version__ = "{{cookiecutter.version}}"


def create_app(test_config=None):

    # cria e configura a aplicacao
    app = Flask(__name__, instance_relative_config=True)

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
    Swagger(app, template_file=os.path.join(os.getcwd(), 'app', 'docs', 'template.yml'), parse=True)
    CORS(app)

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
