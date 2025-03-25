
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
get = load_dotenv()
FROM_EMAIL = os.environ.get("EMAIL_ADDRESS")
TO_EMAIL = os.environ.get("TO_EMAIL_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Opera\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0",
}


response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=HEADERS)
web_answer = response.text


soup = BeautifulSoup(web_answer, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText()
print(soup.prettify())
price_without_currency = price.split("$")[1]
message = "Time to buy price lower than 100$"

price_as_float = float(price_without_currency)

if price_as_float < 100 :
    with smtplib.SMTP("smtp.gmail.com", port = 587) as smtp:
        smtp.starttls()
        smtp.login(FROM_EMAIL,PASSWORD)
        smtp.sendmail(FROM_EMAIL,TO_EMAIL,message.encode("utf-8"))




