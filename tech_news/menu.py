from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys

number_options = {
    "0": lambda x: get_tech_news(
        int(input("Digite quantas notícias serão buscadas:"))
    ),
    "1": lambda x: search_by_title(input("Digite o título:")),
    "2": lambda x: search_by_date(
        input("Digite a data no formato aaaa-mm-dd:")
    ),
    "3": lambda x: search_by_tag(input("Digite a tag:")),
    "4": lambda x: search_by_category(input("Digite a categoria:")),
    "5": lambda x: top_5_news(),
    "6": lambda x: top_5_categories(),
    "7": lambda x: "Encerrando script\n",
}


# Requisito 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    try:
        if option in number_options:
            result = number_options[option](None)
            print(result)
        else:
            sys.stderr.write("Opção inválida\n")
    except Exception as err:
        sys.stderr.write(err)
