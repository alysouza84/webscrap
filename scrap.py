import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/' #url da pagina que queremos fazer o scrap
response = requests.get(url) #faz a requisicao da pagina

#print(response.status_code) #200 significa que a pagina foi carregada com sucesso
#print(response.text) mostra o html da pagina

site = BeautifulSoup(response.text, 'html.parser')

#print(site.prettify()) funcao que mostra o html da pagina de forma mais legivel atribuida a variavel site;

content = response.content #pega o conteudo da pagina

titulo = site.find('title') #pega o titulo da pagina

print(titulo.text) #mostra o titulo da pagina
