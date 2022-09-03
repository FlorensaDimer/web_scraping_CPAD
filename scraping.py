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

for i in range(0,1):
#Entra no url de cada filme separado para coletar dados
    
    url = "https://www.imdb.com"+ str(filmes[i].a["href"])
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
    
    # titulo = soup.find(class_="sc-b73cd867-0 eKrKux")
    # #Encontrao conteudo do "soup" usando parametros, find busca somente o 1°
    # print("titulo")
    # print(titulo.string)
        
    # anoLancamento = soup.find(class_="sc-8c396aa2-2 itZqyK")
    # #Encontrao conteudo do "soup" usando parametros, find busca somente o 1°
    # print("anoLancamento")
    # print(anoLancamento.string)
    
    # urlPoster = soup.find(class_="ipc-lockup-overlay ipc-focusable")
    # #Encontrao conteudo do "soup" usando parametros
    # print("urlPoster")
    # print(urlPoster["href"])
 
    imagemPoster = soup.find(class_="ipc-lockup-overlay ipc-focusable")
    #Encontrao conteudo do "soup" usando parametros Conferir+++++++
    print("imagemPoster")
    print(imagemPoster["href"])
    
    # notaImdb = soup.find(class_="sc-7ab21ed2-1 jGRxWM")
    # #Encontrao conteudo do "soup" usando parametros
    # print("notaImdb")
    # print(notaImdb.string)

    # listaGeneros = soup.find_all(href="/name/nm0001104/?ref_=tt_cl_dr_1")
    # #Encontrao conteudo do "soup" usando parametros
    # print("listaGeneros")
    
    # for item in listaGeneros:
    #     #Passa por todos os filmes e pega as partes a[href]
    #     print(item.string)
        
    # listaDiretores = soup.find_all()
    # #Encontrao conteudo do "soup" usando parametros Conferir+++++++
    # # tds = soup.find_all(class_="w2p_fw") #find all faz uma lista
    # print("listaDiretores")
  
    # for item in  listaDiretores:
    #     #Passa por todos os filmes e pega as partes a[href]
    #     print(item.string)
 

# %%
