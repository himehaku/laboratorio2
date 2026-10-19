import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
respuesta = requests.get(URL, timeout=10)
respuesta.raise_for_status()
soup = BeautifulSoup(respuesta.text, "html.parser")
# Complete los selectores y la extracción.
print(respuesta.url)



libros_data = []

libros = soup.find_all("article", class_="product_pod")

for libro in libros:
    titulo = libro.h3.a["title"]
    precio = libro.find("div", class_="product_price").find("p", class_="price_color").text
    disponibilidad = libro.find("div", class_="product_price").find("p",  class_="instock availability").text
    calificacion = libro.p.text

    libros_data.append("Título: " + titulo)
    libros_data.append("Precio: " + precio)
    libros_data.append("Disponibilidad: " + disponibilidad)
    libros_data.append("Calificacion: " + calificacion)




print("\n".join(libros_data))