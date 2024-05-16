from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = JOB_LINKEDIN_WEB

EMAIL = YOUR_EMAIL
PASSWORD = PASSWORD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Log In
login_btn = driver.find_element(By.CSS_SELECTOR, value=".btn-secondary-emphasis")
login_btn.click()

# Reject Cookies
time.sleep(2)
reject_cookies = driver.find_element(By.XPATH, value='/html/body/div/main/div[1]/div/section/div/div[2]/button[2]')
reject_cookies.click()

# Fill Email & Password
email = driver.find_element(By.NAME, value="session_key")
password = driver.find_element(By.NAME, value="session_password")
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
time.sleep(2)
password.send_keys(Keys.ENTER)

# Save Jobs
job_listing = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
print(len(job_listing))
for job in job_listing:
    time.sleep(1)
    job.click()
    save_btn = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    save_btn.click()






