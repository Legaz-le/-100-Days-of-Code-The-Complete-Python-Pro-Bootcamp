from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
import time

LINK_TO_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScv7mvbiy60cLv0XfnQyTkLNc6hbTMhC26huJcKedydtxnrzg/viewform?usp=sf_link"


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
website_answer = response.text

#Finding elements on the website
soup = BeautifulSoup(website_answer, "html.parser")
rent_price = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in rent_price if "$" in price.text]


rent_link = soup.find_all("a", class_="property-card-link")
all_links = [link.get("href") for link in rent_link]

rent_address = soup.select("a address")
all_address = [address.text.replace(" | ", " ").strip() for address in rent_address]
#Fill the form
Chrome_option = ChromiumOptions()
Chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome()




for i in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScv7mvbiy60cLv0XfnQyTkLNc6hbTMhC26huJcKedydtxnrzg/viewform")
    time.sleep(2)
    what_address_fill_in = driver.find_element(By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    what_price_fill_in = driver.find_element(By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    what_link_fill_in = driver.find_element(By.XPATH,
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    button = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
    what_address_fill_in.send_keys(all_address[i])
    what_price_fill_in.send_keys(all_prices[i])
    what_link_fill_in.send_keys(all_links[i])
    button.click()














