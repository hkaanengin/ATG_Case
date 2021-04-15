from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import csv

bot = webdriver.Chrome()

bot.get("https://azcargo.cz/en/services/support/iata-airline-codes/")
time.sleep(1)
eles=bot.find_element_by_xpath('//table[@class="table table--code table--airline"]/tbody')

all_eles=eles.find_elements_by_xpath('./tr')
iata_code_list=[]
for i in all_eles:
    iata_code=i.find_elements_by_xpath('./td')[1].text.split(' ')[2]
    airline_name=i.find_elements_by_xpath('./td')[2].text
    iata_code_list.append([iata_code,airline_name])
time.sleep(1)

rest_file="IATA_CODES.csv"
with open(rest_file, 'w', encoding='UTF-8', newline="") as csv_file:
    wr = csv.writer(csv_file)
    wr.writerows(iata_code_list)