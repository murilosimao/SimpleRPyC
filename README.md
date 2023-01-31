<h1 align="center">Server RPyC Using Python</h1>

<br>

## :dart: Sobre ##

RPC é uma técnica bem classica na computação que significa chamada remota de métodos, ou seja, temos um servidor com uma série de métodos, que um computador ou uma aplicação não conseguiria fazer, então esse computador/aplicação chama um método implementado no servidor.

## :sparkles: Features ##

:heavy_check_mark: RPyC - Usado para fazer o servidor RPC\
:heavy_check_mark: Docker - Utilizado para escalar

## :rocket: Tecnologias ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [RPyC](https://rpyc.readthedocs.io/en/latest/)


## :checkered_flag: Iniciando ##

```bash
# Clone o repositório

# Contrua a imagem Docker a partir da pasta server
$ docker build --tag serverrpc:msimao .

# Rode o container
$ docker run -p 18811:18811 serverrpc:msimao

# Rode o rpyc-client.py
$ python rpyc-client.py
```

## :memo:  ##

Made with :heart: by <a href="https://github.com/murilosimao" target="_blank">MuriloSimão</a>

&#xa0;

<a href="#top">Ir para o ínicio</a>
