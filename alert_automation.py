import time
from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\Vishnu\PycharmProjects\python_learning\chromedriver.exe")
driver.get("url")
driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
