from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time



response = requests.get("https://steamcharts.com/top")
yc_website  = response.text

soup = BeautifulSoup(yc_website, "html.parser")

name_of_game = [game.getText().strip() for game in soup.find_all("td", class_="game-name left")]
peak_of_players = [peak.getText() for peak in soup.find_all("td",class_="num period-col peak-concurrent")]
hours_played = [players.getText() for players in soup.find_all("td", class_="num period-col player-hours")]
print(name_of_game)
print(peak_of_players)
print(hours_played)

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
for n in range (len(name_of_game)):
    driver.get("LINK for CSV")
    time.sleep(2)

    game = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    peak = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    hours = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    game.send_keys(name_of_game[n])
    peak.send_keys(peak_of_players[n])
    hours.send_keys(hours_played[n])
    submit.click()
