import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/' #url da pagina que queremos fazer o scrap

response = requests.get(url) #faz a requisicao da pagina
content = response.content

resposta = response.status_code #200 significa que a pagina foi carregada com sucesso
if resposta == 200:
    print('Pagina carregada com sucesso')

site = BeautifulSoup(content, 'html.parser') #faz o parse do conteudo da pagina

#print(site.prettify()) #funcao que mostra o html da pagina de forma mais legivel atribuida a variavel site;

noticias = site.findAll('div', attrs={'class': 'feed-post-body'}) #pega todas as noticias da pagina

print(site.title.get_text()) #mostra o titulo da pagina 

for i, noticia in enumerate(noticias, start=1):
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'}) #pega o titulo da noticia
    print(f'Noticia {i}: {titulo.text}') #mostra o titulo da noticia