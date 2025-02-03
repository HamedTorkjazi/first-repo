import requests
from bs4 import BeautifulSoup
import os

URL = "https://cebit.ir/search/asus-laptop"

Response = requests.get(URL)
print(Response.status_code)

soup = BeautifulSoup(Response.text,"html.parser")

Products = soup.find_all('div', "col col-12 col-md-4 col-ld-6 col-eld-4 col-beld-3 items")

Information = open("Information.txt", "w",encoding='utf-8')
os.makedirs("images")

for index,prod in enumerate(Products):

    #Title
    title = prod.find("h3", class_="title-fa rb")
    for t in title:
        Information.write(f"{index + 1}.\tTitle: {t}\n\n")

    #Value
    value = prod.find("span", class_="value").text.strip()
    Information.write(f"\tValue: {value}\n\n")

    #Link
    links = prod.find_all("a", href = True)
    for link in links:
        Information.write(f"\tLink: {link["href"]}\n\n----------------------------------------------------------------------------------------------------------------------\n\n")

    #Image
    images = prod.find_all("img", src = True)
    image_path = os.path.join("images", f"{index + 1}.jpg")
    folder = open(image_path, "wb")

    for address in images:
        Response = requests.get(url = address["src"])
        folder.write(Response.content)


Information.close()
folder.close()
