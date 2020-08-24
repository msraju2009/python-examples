from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(r"path\chromedriver.exe")
driver.get("https://www.flipkart.com/")
x=driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/ul/li[1]/span")
y=driver.find_element_by_xpath("//*[contains(@title,'Mobiles')]")
# z=driver.find_element_by_xpath("xpath")
actions=ActionChains(driver)
actions.move_to_element(x).move_to_element(y).click().perform()
