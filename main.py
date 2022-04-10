import lxml
import smtplib
from bs4 import BeautifulSoup
import requests
URL ="https://www.amazon.com/Kitchen-Settings-Dishwasher-safe-BPA-Free-Processor/dp/B09DZ39TY5/ref=sr_1_2_sspa?crid=28CG4N0AS8777&keywords=BLENDER&qid=1649605024&sprefix=blender%2Caps%2C421&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5OFA3UjNWOFRLOE0mZW5jcnlwdGVkSWQ9QTAxMzI2NDBSV0NXVVZRUFJPM0ImZW5jcnlwdGVkQWRJZD1BMDI1MDE3MEFBR1NMS1dYQVBKOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent ": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                   " Chrome/100.0.4896.75 Safari/537.36"
}
response = requests.get(url=URL, headers=HEADERS)
amazon_webpage = response.text
print(amazon_webpage)
soup = BeautifulSoup(amazon_webpage, "html.parser")
#print(soup.prettify())
blender_price = soup.find(name="span",class_="a-offscreen")
print(blender_price.get_text())

blender_price_without_currency = blender_price.split("$")[1]
blender_price_as_float = float(blender_price_without_currency)
print(blender_price_as_float)

title = soup.find(id="productTitle").get_text().strip()
BUY_PRICE = 200

if blender_price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )