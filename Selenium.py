from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
date = date.today().strftime("%-m-%-d-%Y")
url = "https://www.chabad.org/calendar/candlelighting_cdo/aid/6226/locationid/11365/locationtype/2/save/1/tdate/" + date + "/jewish/Shabbat-Candle-Lighting-Times.htm"
driver.get(url)
ShabbosTime = driver.find_element(By.CLASS_NAME, "time").text
print(ShabbosTime)
