from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "D:\chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--window-size=500,500")

driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

driver.get("http://practice.automationtesting.in/")
print(driver.current_url)

driver.quit()