import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://web.telegram.org"

opt = webdriver.FirefoxOptions()
web = webdriver.Firefox(options=opt)

btn = "none"
while btn == 'none':
    try:
        web.find_element(By.CSS_SELECTOR, ".Button").click()
    except:
        time.sleep(3)

web.find_element(By.CSS_SELECTOR, "div.input-group:nth-child(1)").send_keys("Uzbekistan")
phone_num = input("Phone Number : ")
web.find_element(By.CSS_SELECTOR, '#sign-in-phone-number').send_keys(phone_num)
web.find_element(By.CSS_SELECTOR, "button.Button:nth-child(4) > div:nth-child(1)").click()
time.sleep(10)
verification_code = input(f"Telegram Verification code on {phone_num} : ")
web.find_element(By.CSS_SELECTOR, "#sign-in-code").send_keys(verification_code)
web.find_element(By.CSS_SELECTOR, "#sign-in-code").send_keys(Keys.ENTER)

