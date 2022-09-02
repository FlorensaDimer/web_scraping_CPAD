# %%
import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
#Url dos 250
request = urllib.request.Request(url)
#Request para entrar no url

request.add_header("User-agent", "cpa-dados")
#Realizar o request com o usuario nomeado "cpa-dados"

response = urllib.request.urlopen(request)
#Abre a pagina do url

response_encoding = response.headers.get_content_charset()
#Pega conteudo da pagina

response_content = response.read().decode('utf-8')
#Decodifica o conteudo

soup = BeautifulSoup(response_content, 'html.parser')
#Processo de analisar um texto para determinar sua estrutura lógica

filmes = soup.find_all(class_="titleColumn")
#Encontrao conteudo do "soup" usando parametros
#Encontrou todos os links dos filmes, cria uma lista

for item in filmes:
#Passa por todos os filmes e pega as partes a[href]
    print(item.a['href'])

for i in range(1,5):
#Entra no url de cada filme separado para coletar dados

    url = "https://www.imdb.com"+str(item.a['href'])
    #Url base("https://www.imdb.com") + caminho obtido pelo link (str(item.a['href']))
    #Url dos 250
    
    request = urllib.request.Request(url)
    #Request para entrar no url

    request.add_header("User-agent", "cpa-dados")
    #Realizar o request com o usuario nomeado "cpa-dados"

    response = urllib.request.urlopen(request)
    #Abre a pagina do url

    response_encoding = response.headers.get_content_charset()
    #Pega conteudo da pagina

    response_content = response.read().decode('utf-8')
    #Decodifica o conteudo

    soup = BeautifulSoup(response_content, 'html.parser')
    #Processo de analisar um texto para determinar sua estrutura lógica

    titulo = soup.find_all(class_="sc-b73cd867-0 fbOhB")
    #Encontrao conteudo do "soup" usando parametros
    
    anoLancamento = soup.find_all(class_="ipc-inline-list__item")
    #Encontrao conteudo do "soup" usando parametros
    
    urlPoster = soup.find_all(class_="ipc-lockup-overlay__screen")
    #Encontrao conteudo do "soup" usando parametros
    
    imagemPoster = soup.find_all(class_="ipc-lockup-overlay__screen")
    #Encontrao conteudo do "soup" usando parametros Conferir+++++++
    
    notaImdb = soup.find_all(class_="sc-7ab21ed2-1 jGRxWM")
    #Encontrao conteudo do "soup" usando parametros

    listaGeneros = soup.find_all(class_="ipc-inline-list__item")
    #Encontrao conteudo do "soup" usando parametros
    
    listaDiretores = soup.find_all(class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
    #Encontrao conteudo do "soup" usando parametros Conferir+++++++
# tds = soup.find_all(class_="w2p_fw") #find all faz uma lista

# %%
