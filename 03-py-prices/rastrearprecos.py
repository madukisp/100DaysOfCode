import requests
from lxml import html
import json
import os

def get_price_from_amazon(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(product_url, headers=headers)
    tree = html.fromstring(response.content)

    price_xpath_whole = '//span[@class="a-price-whole"]/text()'
    price_xpath_fraction = '//span[@class="a-price-fraction"]/text()'
    
    price_cash_whole = tree.xpath(price_xpath_whole)
    price_cash_fraction = tree.xpath(price_xpath_fraction)
    
    if price_cash_whole and price_cash_fraction:
        price_cash = price_cash_whole[0].strip() + '.' + price_cash_fraction[0].strip()
        try:
            return float(price_cash.replace('.', '').replace(',', '.'))
        except ValueError:
            print(f"Erro ao converter o preço da Amazon: {price_cash}")
            return float('inf')
    else:
        print("Preço da Amazon não encontrado")
        return float('inf')

def get_price_from_magalu(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(product_url, headers=headers)
    tree = html.fromstring(response.content)

    price_xpath = '/html/body/div[1]/div/main/section[5]/div[6]/div/div/div/div/p'
    price_cash = tree.xpath(price_xpath)
    if price_cash:
        price_cash = price_cash[0].text
        try:
            return float(price_cash.replace('R$', '').replace('.', '').replace(',', '.').strip())
        except ValueError:
            print(f"Erro ao converter o preço da Magazine Luiza: {price_cash}")
            return float('inf')
    else:
        print("Preço da Magazine Luiza não encontrado")
        return float('inf')

def save_prices(amazon_price, magalu_price):
    prices = {
        "amazon": amazon_price,
        "magalu": magalu_price
    }
    with open("prices.json", "w") as file:
        json.dump(prices, file)

def load_prices():
    if os.path.exists("prices.json"):
        with open("prices.json", "r") as file:
            return json.load(file)
    return {"amazon": float('inf'), "magalu": float('inf')}

def main():
    amazon_url = "https://www.amazon.com.br/LG-Bluetooth-compat%C3%ADvel-Intelig%C3%AAncia-Artificial/dp/B095PY7423/ref=sr_1_5?crid=3IBFQMF6ZPDZ8&dib=eyJ2IjoiMSJ9.i2az3yIAYkGBIlGnbLCbeIU4wdHCDh_PXoLoOrufzq-KMVekM7-8FNGdQ3Lm65cVsn1zWxWuwqXTyBRJj-liRYI9U3zw9x1xjHK-EWTgVKuMPTlLvX6FrFHOyauIItcuPEIlqFAl3XIDBDpN6TaMxZ_pZa9rKHponG2FFmoG9vxt4hYoxXgDQg5LURD1oI6RrFbvp6Q5aMvAddqWiKyq38G-wPMQtwibWn4hRSr6N_Psen2iy27iDv01TbNy8ozpuVJvTIyT5NDwEkr3s0aS1HlByu6KOv-eaH2Eh1hhDt8.x3AxO1JeXwEcsxQEZaVHuWaJFqz4BBTDENbE6ndBYtY&dib_tag=se&keywords=tv+lg+43&qid=1721666937&sprefix=tv+lg%2Caps%2C398&sr=8-5&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751"
    magalu_url = "https://www.magazineluiza.com.br/smart-tv-43-lg-full-hd-43lm6370-wifi-bluetooth-hdr-thinqai-compativel-com-inteligencia-artificia-lg-eletronics/p/ke0g256cjg/et/elit/?&seller_id=maniavirtual&utm_source=google&utm_medium=pla&utm_campaign=&partner_id=75436&gclsrc=aw.ds&gclid=CjwKCAjwhvi0BhA4EiwAX25uj4GAz_pfrrAfcPSeFmMDcD78Out8HWYcl_BFXBk8BSS8ubWxZ1YnWRoCzIUQAvD_BwE"

    amazon_price_cash = get_price_from_amazon(amazon_url)
    magalu_price_cash = get_price_from_magalu(magalu_url)

    previous_prices = load_prices()

    if amazon_price_cash < previous_prices["amazon"]:
        print(f"Amazon - Novo preço mais baixo: R${amazon_price_cash:.2f} (Anterior: R${previous_prices['amazon']:.2f})")
    else:
        print(f"Amazon - Preço à vista: R${amazon_price_cash:.2f}")

    if magalu_price_cash < previous_prices["magalu"]:
        print(f"Magazine Luiza - Novo preço mais baixo: R${magalu_price_cash:.2f} (Anterior: R${previous_prices['magalu']:.2f})")
    else:
        print(f"Magazine Luiza - Preço à vista: R${magalu_price_cash:.2f}")

    save_prices(amazon_price_cash, magalu_price_cash)

if __name__ == "__main__":
    main()
