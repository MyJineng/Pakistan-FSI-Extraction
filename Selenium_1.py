from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

url = 'https://www.sbp.org.pk/ecodata/index2.asp'
browser = webdriver.Firefox()
browser.get(url)

download = browser.find_element(By.XPATH, '//a[contains(@href, "DDholders-Arc.xls")]')
download.click()

excel_links = browser.find_elements(By.XPATH, '//a[contains(@href, "DDholders-Arc.xls")]')

for link in excel_links:
    url = link.get_attribute('href')
    filename = url.split('/')[-1]
    xls = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(xls.content)
    print(f'{filename} downloaded.')

browser.close()

# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# url = 'https://www.sbp.org.pk/ecodata/index2.asp'
# browser = webdriver.Chrome(executable_path = 'C:\PycharmProjects\chromedriver_win32\chromedriver.exe')
# browser.get(url)
#
# # browser.find_element_by_xpath('//a[contains(text(), " Deposits Distributed by Category of Deposit Holders")]').click()
#
# excel_links = browser.find_elements_by_xpath('//a[contains(@href, "DDholders-Arc.xls")]')
#
# for link in excel_links:
#     url = link.get_attribute('href')
#     filename = url.split('/')[-1]
#     xls = requests.get(url)
#     with open(filename, 'wb') as f:
#         f.write(xls.content)
#     print(f'{filename} downloaded.')