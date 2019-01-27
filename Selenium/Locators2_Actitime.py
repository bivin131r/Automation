from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("http://localhost/login.do")
'''This  below line is for finding element by Class Name on Pracrise.HTML page'''
driver.find_element_by_class_name("")