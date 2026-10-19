import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
respuesta = requests.get(URL, timeout=10)
respuesta.raise_for_status()
soup = BeautifulSoup(respuesta.text, "html.parser")
# Complete los selectores y la extracción.
print(respuesta.url)

contenedor_t = soup.select_one("#content_inner > article > div.row > div.col-sm-6.product_main")

titulo = contenedor_t.find("h1")

print(titulo.get_text)