

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import  By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SIMILAR_ACCOUNT = "https://www.instagram.com/chefsteps/"
USERNAME = "xxxxxx"
PASSWORD = "xxxxxxx"
goal = 100

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        press_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        press_button.click()
        time.sleep(4)
        dismiss_button = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Не сейчас')]")
        if dismiss_button:
            dismiss_button.click()



    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(3)
        follower_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        follower_button.click()
        time.sleep(3)
        # find_window = self.driver.find_element(By.CSS_SELECTOR, '.xyi19xy')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", find_window)
        #     time.sleep(15)

    def follow(self):
        follow_button = self.driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button")
        for button in follow_button:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
