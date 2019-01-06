from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Python_Selenium/Practise.html")
time.sleep(10)
driver.find_element(By.XPATH,"//input[contains(@id,'Python')]").click()
time.sleep(10)
driver.close()