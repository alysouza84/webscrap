import requests
from bs4 import BeautifulSoup

url = 'https://www.cnnbrasil.com.br/' #url da pagina que queremos fazer o scrap

response = requests.get(url) #faz a requisicao da pagina
content = response.content

resposta = response.status_code #200 significa que a pagina foi carregada com sucesso
if resposta == 200:
    print('Pagina carregada com sucesso')
    
site = BeautifulSoup(content, 'html.parser') #faz o parse do conteudo da pagina

#print(site.prettify()) #funcao que mostra o html da pagina de forma mais legivel atribuida a variavel site;

noticias = site.findAll('h3', attrs={'class': 'block__news__title'}) #pega todas as noticias da pagina

print(site.title.get_text()) #mostra o titulo da pagina

print()

for i, noticia in enumerate(noticias, start=1):
    titulo = noticia.get_text().strip() #pega o titulo da noticia
    if titulo:
        print(f'Noticia {i}: {titulo}') #mostra o titulo da noticia