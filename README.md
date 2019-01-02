# Flask Skeleton API

Um simples esqueleto de API construido com Flask.

## About

Este é um esqueleto de API construido com Flask e utilizado pelo Núcleo de Tecnologia e Inovação do Grupo Ceuma (NTI) para a construção de aplicações backend.

## Documentação

Para acessar a documentação da API, acesse a seguinte rota:

```
http://localhost:5000/app-name/apidocs/
```

A API possui um arquivo de documentação *default* utilizando a especificação do *[Blueprint](https://apiblueprint.org/)*.
O arquivo está em: *./app/docs/api-blueprint-sample.apib*.

Preferimos deixar a responsabilidade da renderização do template HTML para o desenvolvedor.
Toda vez que houver atualizações na especificação de endpoints da sua API, será de responsabilidade do desenvolvedor realizar a atualização e renderização do documento estático.
Para isso, basta utilizar as ferramentas existentes e sugeridas pelo *[Blueprint](https://apiblueprint.org/)*.

Afim de facilitar o processe de gerar o HTML, descrevemos ele a seguir.

### 1. Instale o *Render*

Uma das ferramentas sugeridas pelo Blueprint é o [Aglio](https://github.com/danielgtaylor/aglio). Usaremos ele:

```npm install -g aglio```

### 2. Gere a documentação.

Para isso, entre na raíz do projeto e execute o seguinte comando:

```
aglio -i ./app/docs/api-blueprint-sample.apib --theme-full-width --no-theme-condense -o ./app/templates/apidocs/index.html
```

O Output será um arquivo ```ìndex.html``` dentro de ```./app/templates/apidocs/index.html```.

*p.s: O arquivo base para esta documentação, foi retirado de: [Definindo APIs com o API Blueprint](https://eltonminetto.net/post/2017-06-29-definindo-apis-com-api-blueprint/)*.

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
