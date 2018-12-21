# Flask Skeleton API

Um simples esqueleto de API construido com Flask.

### About

Este é um esqueleto de API construido com Flask e utilizado pelo Núcleo de Tecnologia e Inovação do Grupo Ceuma (NTI) para a construção de aplicações backend.

## Como usar isto

### Usando Flask

```export FLASK_APP=app```

Para ativar o modo de Debug faça:

```export FLASK_ENV=development```

*p.s: é aconselhável que você esteja utilizando uma virtualenv para a execução do projeto.*

### Usando Docker

Para subir a aplicação usando docker, basta executar o seguinte comando na raíz do projeto:

```docker-compose up -d --build```

O arquivo ```docker-compose.yml``` usa o [ceumanti/docker-python-odbc](https://hub.docker.com/r/ceumanti/docker-python-odbc), uma imagem preparada para com configuração de conexão com SQLServer usando a versão 3.6.5 do Python.
A imagem é extensível e qualquer pessoa pode criar outras imagens a partir dela. Recomendamos que sejam criadas imagens a partir desta, por conta do processo de construção usando Pyenv, que é custosa.

## Maintainers and Contributors

Este projeto é mantido por [@devsceuma](https://github.com/devsceuma).

### Maintainers

[Igor Cavalcanti](https://github.com/cavalcantigor) <br>
[Atmos Maciel](https://github.com/atmosmps)

### Como contribuir

Qualquer pessoa pode contribuir com este projeto, basta fazer um fork do repositório e submeter Pull Requests; :)

## [License](./LICENSE)

Este projeto está sob uma Licença [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0)
