from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(r"add chrome path\chromedriver.exe")
driver.get("url")
element=driver.find_element_by_xpath("xpath")
x=Select(element)
x.select_by_visible_text("text")
x.select_by_index(index)
x.select_by_value("value in html")
