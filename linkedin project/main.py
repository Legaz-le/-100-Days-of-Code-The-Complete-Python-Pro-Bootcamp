from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4086224321&f_AL=true&keywords=Web%20Programmer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
sleep(5)
second_log_in =  driver.find_element(By.CLASS_NAME, "nav__button-secondary.btn-secondary-emphasis.btn-md")
second_log_in.click()
input_username_in = driver.find_element(By.ID,"username")
input_password_in = driver.find_element(By.ID, "password")
input_username_in.send_keys("worldhaha@mail.ru")
input_password_in.send_keys("123456789Asd")
press_button = driver.find_element(By.CLASS_NAME,"btn__primary--large.from__button--floating")
press_button.click()
sleep(3)
save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3")
save_button.click()
while True:
    next_job = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for price in next_job:
        price.click()
        sleep(2)
        save_button = driver.find_element(By.CLASS_NAME,"jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3")
        save_button.click()


