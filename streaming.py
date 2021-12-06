from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def stream_search(search):
    """
    Nesta aplicação selenium é possivel saber em qual streaming há determinado filme/serie/anime
    Para isso, usa-se o site 'justwatch'
    """
    # Configuração do selenium e beautifulsoup:
    option = Options()
    option.add_argument('--headless')

    browser = webdriver.Chrome(options=option)
    browser.get('https://www.justwatch.com/br/busca?q=' + search)
    site = BeautifulSoup(browser.page_source, 'html.parser')

    # Procurando o filme e verificando se existe:
    movie = site.find('ion-row', attrs={'class': 'title-list-row__row md hydrated'})

    if not movie:
        return f'{search} não esta disponivel no nosso catalogo, ou nao existe'

    # Nome do filme e dos streamings
    movie_name = movie.find('a', attrs={'class': 'title-list-row__row-header'}).text
    stream_list = movie.find('div', attrs={'class': 'price-comparison__grid__row__holder'})

    # Trabalhando com os dados dos streamings
    if not stream_list:
        return f'{movie_name} não esta disponivel em nenhum serviço de streaming'

    streamings = stream_list.findAll('img')

    stream_names = []

    for streaming in streamings:
        stream_names.append(streaming['title'])

    return f'{movie_name} está disponivel nestes streamings: '+", ".join(stream_names)