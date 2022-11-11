# Projeto Tech News

Esse projeto foi realizado para exercitar o que foi aprendido na Seção 3 do Módulo de Ciência da Computação do curso da [Trybe](https://www.betrybe.com/), no qual foi sobre `Arquitetura de Redes` e `Raspagem de Dados` utilizando a linguagem de programação `Python`.

Neste projeto foi desenvolvido um `web scraper` para fazer a raspagem de dados de notícias encontradas no [blog da Trybe](https://blog.betrybe.com/) para assim armazenar tais dados em um banco de dados utilizando o SGBD `MongoDB`.

## Tecnologias

  - Python
  - requests
  - parsel
  - MongoDB
  - Docker

## Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone git@github.com:Lucas-Almeida-SD/Trybe-Projeto_36-Tech_News.git

$ cd Trybe-Projeto_36-Tech_News
```

Para iniciá-lo, siga os passos abaixo:

<details>
  <summary><strong>Com Docker</strong></summary>

  ```bash
  # Criar containers
  $ docker-compose run --rm news 
  ```

  Para executar a aplicação,  utilize o terminal interativo do container da aplicação e insira o comando abaixo:
  ```bash
  $ tech-news-analyzer
  ```

  Será exibido um menu no seguinte formato:

        Selecione uma das opções a seguir:
            0 - Popular o banco com notícias;
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por tag;
            4 - Buscar notícias por categoria;
            5 - Listar top 5 notícias;
            6 - Listar top 5 categorias;
            7 - Sair.

</details>

<details>
  <summary><strong>Sem Docker</strong></summary>

  Aqui será necessário possuir o SGBD __MongoDB__ instalado em sua máquina e rodando na porta `27017`.

  ```bash
  # criar o ambiente virtual
  $ python3 -m venv .venv

  # ativar o ambiente virtual
  $ source .venv/bin/activate

  # instalar as dependências no ambiente virtual
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Para executar a aplicação,  utilize o terminal e insira o comando abaixo:

  ```bash
  $ tech-news-analyzer
  ```

  Será exibido um menu no seguinte formato:

        Selecione uma das opções a seguir:
            0 - Popular o banco com notícias;
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por tag;
            4 - Buscar notícias por categoria;
            5 - Listar top 5 notícias;
            6 - Listar top 5 categorias;
            7 - Sair.
</details>
