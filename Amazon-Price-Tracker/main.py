import lxml
import smtplib
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Axor-Jet-Open-Helmet-Chestnut/dp/B07LCXWFT7/ref=sr_1_9?keywords=axor%2Bhelmets%2Bfor%2Bmen&sr=8-9&th=1"
BUY_PRICE = 2000
headers = {
    "Cookie": "PHPSESSID=a6bf73548845551fdbc40eafbb702fd7",
    "Host": "www.amazon.in",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
flag = True
counter = 0

while flag:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml")

    # checking if response page is not an amazon captcha page
    if soup.find(id="captchacharacters"):
        print(f"Returned Captcha page | Request: {counter+1}")
        counter += 1
    else:
        flag = False

title = soup.select(selector="#productTitle")[0].get_text().strip()
price = soup.select(selector=".a-section .a-price .a-offscreen")[0].get_text()
price_without_currency = price.split("₹")[1].split(",")
price_as_float = float("".join(price_without_currency))

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_email", password="your_password")
