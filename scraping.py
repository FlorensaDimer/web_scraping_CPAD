import urllib.request
import re
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime

# %%

#=====================================================
#Tarefa 1
#=====================================================

url_download = "http://127.0.0.1:8000/places/default/sitemap.xml"
request = urllib.request.Request(url_download)

request.add_header("User-agent", "cpa-dados")

response = urllib.request.urlopen(request)

response_encoding = response.headers.get_content_charset()

response_content = response.read().decode('ascii')

paginas = re.findall("<loc>(.+w\/)", response_content)


with open ('Tarefa_1.csv', 'a') as arq:

    colunas = [
                'National Flag',
                'Area',
                'Population',
                'Iso',
                'Country',
                'Capital',
                'Continent',
                'TId',
                'Currency Code',
                'Currency Name',
                'Phone',
                'Postal Code Format',
                'Postal Code Regex',
                'Languages',
                'Neighbours',
                'Timestamp'
                ]

    for i in range(1,len(paginas)):

        url_download = paginas[i]+str(i)
        request = urllib.request.Request(url_download)

        dt = datetime.now()
        ts = datetime.timestamp(dt)

        request.add_header("User-agent", "cpa-dados")

        response = urllib.request.urlopen(request)

        response_encoding = response.headers.get_content_charset()

        html = response.read().decode('ascii')

        soup = BeautifulSoup(html, 'html.parser')
        
        tds = soup.find_all(class_="w2p_fw") #find all faz uma lista

        urllib.request.urlretrieve("http://127.0.0.1:8000"+str(tds[0].img['src']), "Tarefa_1_imagens\img"+str(i)+".png")

        vizinhos=''
        for string in tds[14].strings:
            vizinhos = vizinhos + string

        dados = {   
                "National Flag":    tds[0].img['src'],
                "Area":             tds[1].string,
                "Population":       tds[2].string,
                "Iso":              tds[3].string,
                "Country":          tds[4].string,
                "Capital":          tds[5].string,
                "Continent":        tds[6].string,
                "TId":              tds[7].string,
                "Currency Code":    tds[8].string,
                "Currency Name":    tds[9].string,
                "Phone":            tds[10].string,
                "Postal Code Format":tds[11].string,
                "Postal Code Regex":tds[12].string,
                "Languages":        tds[13].string,
                "Neighbours":       vizinhos,
                "Timestamp":        ts
                }

        writer = csv.DictWriter(arq, fieldnames=colunas)
        if i==1:
            writer.writeheader()
        writer.writerow(dados)
        
#=====================================================      
##Parte 3
#=====================================================


with open ('Tarefa_1.csv', 'a') as arq:
    url_download = "http://127.0.0.1:8000/places/default/sitemap.xml"
request = urllib.request.Request(url_download)

request.add_header("User-agent", "cpa-dados")

response = urllib.request.urlopen(request)

response_encoding = response.headers.get_content_charset()

response_content = response.read().decode('ascii')

paginas = re.findall("<loc>(.+w\/)", response_content)

lista = arq.readlines()
#Lista se refere ao conteudo de todas as linhas, cada linha uma lista
    
for i in range(1,len(paginas)):
#Pagina(i), Linha(l)   
#i ja serve tambem para index() da lista, ja que verificaremos pagina e linha iguais  
    url_download = paginas[i]+str(i)
    request = urllib.request.Request(url_download)

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    request.add_header("User-agent", "cpa-dados")

    response = urllib.request.urlopen(request)

    response_encoding = response.headers.get_content_charset()

    html = response.read().decode('ascii')

    soup = BeautifulSoup(html, 'html.parser')
    
    tds = soup.find_all(class_="w2p_fw") #find all faz uma lista

    urllib.request.urlretrieve("http://127.0.0.1:8000"+str(tds[0].img['src']), "Tarefa_1_imagens\img"+str(i)+".png")

    vizinhos=''
    for string in tds[14].strings:
        vizinhos = vizinhos + string


    for j in range (0, len(lista),2):
        subLista = lista[i].split(',')
        #SubLista é os elementos de uma linha(lista[index]), separados por split
        for s in range (0, (len(subLista)-1)):
        #SubLista(s)
            if float(subLista[s]) != tds[s].string:
                if s==0:
                    subLista[s] = tds[s].string
                    dt = datetime.now()
                    ts = datetime.timestamp(dt)
                    subLista[:-1] = ts
                    #Sobrescreve o valor da liha (lista[index]) com valores novos, atraves da manipulação de subLista
    
    with open ('Tarefa_1.csv', 'w') as arq:          
        writer.writerows(lista)
        
# %%  

#=====================================================
##Tarefa 2    
#=====================================================


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
# print(len(filmes))

posters = soup.find_all(class_="posterColumn") 

arq_open = open("Tarefa_2.json", "w")

for i in range(0, len(filmes)):
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

    titulo = soup.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-ca85a21c-0.efoFqn > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > h1")
    #Encontrao conteudo do "soup" usando parametros, find busca somente o 1°
    # print("titulo")
    print(titulo[0])
        
    anoLancamento = soup.find(class_="sc-8c396aa2-2 itZqyK")
    #Encontrao conteudo do "soup" usando parametros, find busca somente o 1°
    # print("anoLancamento")
    # print(anoLancamento.string)

    urlPoster = soup.find(class_="ipc-lockup-overlay ipc-focusable")
    #Encontrao conteudo do "soup" usando parametros
    # print("urlPoster")
    # print(urlPoster["href"])

    urllib.request.urlretrieve(str(posters[i].a.img['src'].rpartition('._')[0]+str('.jpg')), 'Tarefa_2_imagens/img'+str(i)+'.jpg')

    notaImdb = soup.find(class_="sc-7ab21ed2-1 jGRxWM")
    #Encontrao conteudo do "soup" usando parametros
    # print("notaImdb")
    # print(notaImdb.string)

    listaGeneros = soup.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-ca85a21c-0.efoFqn > section > div:nth-child(4) > section > section > div.sc-2a827f80-2.kqTacj > div.sc-2a827f80-10.fVYbpg > div.sc-2a827f80-4.bWdgcV > div.sc-16ede01-8.hXeKyz.sc-2a827f80-11.kSXeJ > div > div.ipc-chip-list__scroller > a > span")
    #Encontrao conteudo do "soup" usando parametros (usando o selector path)
    # print("listaGeneros")

    for i in range (0, len(listaGeneros)):
        #Passa por todos os filmes e pega as partes a[href]
        if i ==0 and (listaGeneros[i].string != None):
            Generos = listaGeneros[i].string
        elif i == len(listaGeneros) and (listaGeneros[i].string != None):
            Generos = ", "+listaGeneros[i].string
        elif listaGeneros[i].string != None:
            Generos = Generos+", "+listaGeneros[i].string
        
    listaDiretores = soup.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-ca85a21c-0.efoFqn > section > div:nth-child(4) > section > section > div.sc-2a827f80-2.kqTacj > div.sc-2a827f80-10.fVYbpg > div.sc-2a827f80-4.bWdgcV > div.sc-fa02f843-0.fjLeDR > ul > li:nth-child(1) > div > ul > li")
    #Encontrao conteudo do "soup" usando parametros (usando o selector path)
    # print("listaDiretores")

    for i in range (0, len(listaDiretores)):
        #Passa por todos os filmes e pega as partes a[href]
        if i ==0 and (listaDiretores[i].string != None):
            Diretores = listaDiretores[i].string
        elif i == len(listaDiretores) and (listaDiretores[i].string != None):
            Diretores = ", "+listaDiretores[i].string
        elif listaDiretores[i].string != None:
            Diretores = Diretores+", "+listaDiretores[i].string
    
    dados = {   
                "titulo": titulo[0].string,
                "Ano de Lancamento":    anoLancamento.string,
                "Url do Poster":        str(posters[i].a.img['src'].rpartition('._')[0]+str('.jpg')),
                "Nota: Imdb":           notaImdb.string,
                "Lista de Generos":     Generos,
                "Lista de Diretores":   Diretores
            }
    #Dicionario com dados extraidos

    json.dump(dados, arq_open, indent = 6)

arq_open.close()   


