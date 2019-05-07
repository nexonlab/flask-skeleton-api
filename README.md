# Flask Skeleton API

Um simples esqueleto de API construido com Flask.

## About

Este é um esqueleto de API construido com Flask e utilizado pelo Núcleo de Tecnologia e Inovação do Grupo Ceuma (NTI) para a construção de aplicações backend.

## Gerar esqueleto utilizando `cookiecutter`

O `cookiecutter` é um utilitário em linha de comando utilizando para gerar templates de projetos criados utilizando a ferramenta.
Para gerar o projeto a partir deste template, você deverá ter o pacote `cookiecutter` instalado no seu python.

1. Instale o `cookiecutter` com o comando `pip install cookiecutter` (aconselhamos o uso de um ambiente virtual python).
2. Execute o comando `cookiecutter https://github.com/devsceuma/flask-skeleton-api` para prosseguir com a geração do template
no diretório atual da execução.
3. Uma vez baixado o projeto, o `cookiecutter` será responsável por gerar o template e para isso irá pedir algumas informações,
entre elas "project_name" que é o nome da pasta do projeto e "app_name" que será o nome da aplicação e prefixo utilizado pela API
em suas rotas.

## Documentação da API

Para acessar a documentação da API, acesse a seguinte rota:

```
http://localhost:5000/app-name/apidocs/
```

A API possui um arquivo de documentação *default* utilizando a especificação do *[Blueprint](https://apiblueprint.org/)*.
O arquivo está em: `./app/docs/api-blueprint-sample.apib`.

Preferimos deixar a responsabilidade da renderização do template HTML para o desenvolvedor.
Toda vez que houver atualizações na especificação de endpoints da sua API, será de responsabilidade do desenvolvedor realizar a atualização e renderização do documento estático.
Para isso, basta utilizar as ferramentas existentes e sugeridas pelo *[Blueprint](https://apiblueprint.org/)*.

Afim de facilitar o processo de gerar o HTML, descrevemos ele a seguir.

### 1. Instale o *Render*

Uma das ferramentas sugeridas pelo *Blueprint* é o [Aglio](https://github.com/danielgtaylor/aglio). Usaremos ele:

```npm install -g aglio```

### 2. Gere a documentação.

Para isso, entre na raíz do projeto e execute o seguinte comando:

```
aglio -i ./app/docs/api-blueprint-sample.apib --theme-full-width --no-theme-condense -o ./app/templates/apidocs/index.html
```

O Output será um arquivo ```index.html``` dentro de ```./app/templates/apidocs/index.html```.

*p.s: O arquivo base para esta documentação foi retirado de: [Definindo APIs com o API Blueprint](https://eltonminetto.net/post/2017-06-29-definindo-apis-com-api-blueprint/)*.

## Como usar isto

### Usando Flask

Antes de iniciar a sua aplicação, você deve informar ao seu terminal qual a aplicação `flask` que será iniciada.
Para isto, você deverar *setar* uma variável de ambiente de nome `FLASK_APP` e, no nosso caso, valor igual a `app`.
Neste caso, o valor `app` refere-se ao módulo python onde está contida a aplicação.

> No Linux:
```
export FLASK_APP=app
```

> No Windows:
```
set FLASK_APP=app
```

Para ativar o modo de debug uma outra variável de ambiente deverá ser setada, desta vez com nome
`FLASK_ENV` e valor `development`. Esta informação informa ao `flask` que ele
deverá iniciar a aplicação em modo de desenvolvimento, com o *stacktrace* de erros
e outras funcionalidades.

> No Linux:
```
export FLASK_ENV=development
```

> No Windows:
```
set FLASK_ENV=development
```

### Usando localmente com Cookiecutter

O cookiecutter permite que o usuário crie projetos a partir de templates, como este Skeleton por exemplo.

1. Para isso você precisa instalar o cookiecutter conforme a [documentação](https://cookiecutter.readthedocs.io/en/latest/index.html) sugere.
De preferência crie um *virtual-env* para isto.

`pip install cookiecutter`

2. Depois gere o novo projeto a partir deste repositório.

`cookiecutter gh:devsceuma/flask-skeleton-api`

Para ver mais formas de uso, visite a sessao de *usage* do [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/usage.html).

#### Virtualenv

É aconselhável que você esteja utilizando uma virtualenv para a execução do projeto. 
No [virtualenvwrapper][1] você encontra a documentação de um utilitário para utilização de ambientes
virtuais com o python. Porém, se você não deseja instalar o utilitário, pode utilizar
apenas o [virtualenv][2] a fim de isolar a instalação dos pacotes do python contido em sua máquina.

### Usando Docker

Para subir a aplicação usando docker, basta executar o seguinte comando na raíz do projeto:

```docker-compose up -d --build```

O arquivo ```docker-compose.yml``` usa o [ceumanti/docker-python-odbc](https://hub.docker.com/r/ceumanti/docker-python-odbc), 
uma imagem preparada para com configuração de conexão com SQLServer usando a versão 3.6.5 do 
Python. A imagem é extensível e qualquer pessoa pode criar outras imagens a partir dela. 
Recomendamos que sejam criadas imagens a partir desta, por conta do processo de construção usando Pyenv, que é custosa.

No processo de contrução e *build* da imagem o *script* `run.sh` será executado. Este *script*, que se
encontra na raíz do projeto, é responsável por efetuar o download e instalação dos pacotes
python, além da execução do servidor `waitress-serve` para rodar a aplicação. A aplicação
dockerizada está pronta para produção (vide utilização de servidor preparado para tal propósito)
e o modo de desenvolvimento está desativado.

### Integração com SQL Server

Esta é uma seção especial destinada a esclarecer alguns processos necessários à utilização
da aplicação em conjunto com o SQL Server.

#### Driver ODBC

> Linux:

Para baixar o driver, você deverá a página
[*ODBC Driver for SQL Server - Linux*](https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017)
e seguir o tutorial.

> Windows:

Para baixar o driver, você deverá a página
[*ODBC Driver for SQL Server - Windows*](https://docs.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-2017)
e seguir o tutorial.

#### Pacote `pyodbc`

Para prosseguir com a instalação, certifique-se de que todo o processo anterior foi corretamente
efetuado. Após isso, o comando

```
pip install pyodbc
```

deverá instalar o pacote `pyodbc` que
será utilizado em conjunto com o driver para acesso à base.

## Maintainers and Contributors

Este projeto é mantido por [@devsceuma](https://github.com/devsceuma).

### Maintainers

[Atmos Maciel](https://github.com/atmosmps) <br>
[Igor Cavalcanti](https://github.com/cavalcantigor)


### Como contribuir

Qualquer pessoa pode contribuir com este projeto, basta fazer um fork do repositório e submeter Pull Requests :)

## [License](./LICENSE)

Este projeto está sob uma Licença [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0)


[1]: <https://virtualenvwrapper.readthedocs.io/en/latest/> "Virtualenvwrapper"
[2]: <https://virtualenv.pypa.io/en/latest/> "Virtualenv"