

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

PROMISED = 10000
PROMISED_UP = 5000
CHROME_DRIVER_PATH = "/user"
X_EMAIL = "xxxxx"
X_PASSWORD = "xxxxxx"

class InternetSpeedXBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down =0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.upload-speed').text


    def x_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(3)
        try:
            account_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            account_email.send_keys(X_EMAIL)
            press_button_continue = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
            press_button_continue.click()
            account_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
            account_password.send_keys(X_PASSWORD)
            press_button_to_login = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
            press_button_to_login.click()
            time.sleep(2)
            tweet = f"Hey internet Provider, why is my internet speed {self.up}up/{self.down}down when i pay for {PROMISED_UP}up/{PROMISED}?"
            post = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            post.send_keys(tweet)
            press_to_tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            press_to_tweet.click()
            time.sleep(100)
        except TimeoutException:
            pass_nickname = self.driver.find_element(By.NAME, 'text')
            pass_nickname.send_keys("legaz200")
            press_button_continue_another = self.driver.find_element(By.XPATH,
        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
            press_button_continue_another.click()
            account_password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'password')))
            account_password.send_keys(X_PASSWORD)
            press_button_to_login = self.driver.find_element(By.XPATH,
        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
            press_button_to_login.click()
            time.sleep(2)
            tweet = f"Hey internet Provider, why is my internet speed {self.up}up/{self.down}down when i pay for {PROMISED_UP}up/{PROMISED}?"
            post = self.driver.find_element(By.XPATH,
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            post.send_keys(tweet)
            press_to_tweet = self.driver.find_element(By.XPATH,
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            press_to_tweet.click()
            time.sleep(10)









bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.x_at_provider()
