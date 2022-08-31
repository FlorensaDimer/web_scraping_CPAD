# %%
import csv
import urllib.request
import re
from bs4 import BeautifulSoup
from datetime import datetime


# %%
url_download = """http://127.0.0.1:8000/places/default/sitemap.xml"""
request = urllib.request.Request(url_download)

request.add_header("User-agent", "cpa-dados")
# %%
response = urllib.request.urlopen(request)
# %%
response_encoding = response.headers.get_content_charset()

response_content = response.read().decode('ascii')
# %%
paginas = re.findall("<loc>(.+w\/)", response_content)

# %%
for i in range(1,len(paginas)):

    url_download = paginas[i]+str(i)
    request = urllib.request.Request(url_download)

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    request.add_header("User-agent", "cpa-dados")

    response = urllib.request.urlopen(request)

    response_encoding = response.headers.get_content_charset()

    html = response.read().decode('ascii')

    soup = BeautifulSoup(html, 'html5lib')
    
    tds = soup.find_all(class_="w2p_fw") #find all faz uma lista


    urllib.request.urlretrieve("http://127.0.0.1:8000"+str(tds[0].img['src']), "img\img"+str(i)+".png")



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

    with open ('dados.csv', 'a') as arq:
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

        writer = csv.DictWriter(arq, fieldnames=colunas)
        if i==1:
            writer.writeheader()
        writer.writerow(dados)