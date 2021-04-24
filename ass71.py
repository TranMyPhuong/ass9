from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")

driver.quit()
