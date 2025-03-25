import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_option)


# Open the Tinder website
driver.get("https://tinder.com")

# Wait for the "Log In" button to be clickable and click it
log_in_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q807713831"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div'))
)
log_in_button.click()

# Wait for the "Accept Cookies" button to be clickable and click it
accept_cookie_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-920667245"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div'))
)
accept_cookie_button.click()

# Wait for the Google login button to be clickable and click it
Facebook_account_login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]'))
)
# Switch to second window to log in
Facebook_account_login_button.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
# log in to Facebook account
login_space = driver.find_element(By.ID, "email")
login_space.send_keys("femewe5992@cantozil.com")
login_password = driver.find_element(By.ID, "pass")
login_password.send_keys("123456789Asd")
click_on_button_login = driver.find_element(By.ID, "loginbutton")
click_on_button_login.click()
press_to_accept_login_section = driver.find_element(By.CLASS_NAME, "x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt")
press_to_accept_login_section.click()

driver.switch_to.window(base_window)
time.sleep(5)
#dismiis all notification
accept_location_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
accept_location_button.click()
notification_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[3]/button[2]/div[2]/div[2]")
notification_button.click()
#swipe
amount = 100
while amount:
    try:
        swipe = driver.find_element(By.CLASS_NAME, "gamepad-icon-wrapper")
        time.sleep(2)
        swipe.click()
    except NoSuchElementException:
        time.sleep(2)
    except ElementClickInterceptedException:
        add_tinder_to_main_page_button = driver.find_element(By.CLASS_NAME, "c9iqosj")
        add_tinder_to_main_page_button.click()


# Wait for a few seconds (you may replace this with further actions or waits)
time.sleep(10)