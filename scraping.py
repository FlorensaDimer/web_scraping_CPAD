# %%
import urllib.request
import re
from bs4 import BeautifulSoup
import csv

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
paginas = re.findall("<loc>(\S+)</loc>", response_content)

# %%
url_download = paginas[31]
request = urllib.request.Request(url_download)

request.add_header("User-agent", "cpa-dados")

response = urllib.request.urlopen(request)

response_encoding = response.headers.get_content_charset()

html = response.read().decode('ascii')

# %%
soup = BeautifulSoup(html, 'html.parser')
# %%
tds = soup.find_all(class_="w2p_fw") #find all faz uma lista

print(tds[0].img['src']) #acessando a primeira aparição da tag td, acessando a tag filha dele e pegando o conteúdo do atributo

for item in tds[1:14]: 
#Mostra todos as informações da pagina
    print(item.string)

# print(tds[14].div.contents)


#============
listaVizinhos = str(tds[14].div.contents).split(',')
#Pega todo o content e separa cada </a>

print('separar')
#Apenas para localizar-me

# print(listaVizinhos[-1])


for i in range(1,len(listaVizinhos)):
#Pega apenas a sigla localizada no link
    if i == 1:
        neighbours = listaVizinhos[i][-7:-5]+','
    elif i == (len(listaVizinhos)-1):
        neighbours = neighbours+' '+listaVizinhos[i][-8:-6]
        #Pega diferente devido ao caracter ] presente no ultimo da lista
    else:
        neighbours = neighbours+' '+listaVizinhos[i][-7:-5]+','
        
        
print (neighbours)
#============



# %%
conteudo = {
    "National Flag":tds[0].img['src'],
    "Area":tds[1].stripped_strings,
    "Population":tds[1].stripped_strings,
    "Iso":tds[3].stripped_strings,
    "Country":tds[4].stripped_strings,
    "Capital":tds[5].stripped_strings,
    "Continent":tds[6].stripped_strings,
    "TId":tds[7].stripped_strings,
    "Currency Code:":tds[8].stripped_strings,
    "Currency Name":tds[9].stripped_strings,
    "Phone":tds[10].stripped_strings,
    "Postal Code Format":tds[11].stripped_strings,
    "Postal Code Regex":tds[12].stripped_strings,
    "Neighbours": neighbours

}
# %%
