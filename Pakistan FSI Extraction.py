from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests

source = "https://www.sbp.org.pk/ecodata/fsi.asp"
browser = webdriver.Firefox()
browser.get(source)

#By Most Recent File

FSI = browser.find_element(By.XPATH, '//a[contains(@href, "xlsx")]')
FSI.click()

Excel = FSI.get_attribute('href')
filename = Excel.split('/')[-1]
xls = requests.get(Excel)
with open(filename, 'wb') as f:
    f.write(xls.content)
    print(f'{filename} downloaded.')

browser.close()

#By Set Number Using Counter
#
# Quarters = 0
# FSI = browser.find_elements(By.XPATH, '//a[contains(@href, ".xlsx")]')
#
# for link in FSI:
#     actions = ActionChains(browser)
#     actions.move_to_element(link).perform()
#     browser.implicitly_wait(5)
#     link.click()
#     url = link.get_attribute('href')
#     filename = url.split('/')[-1]
#     xls = requests.get(url)
#     with open(filename, 'wb') as f:
#         f.write(xls.content)
#     print(f'{filename} downloaded.')
#     Quarters += 1
#     if Quarters == 2:
#         print("All Done!")
#         break
#
# browser.close()