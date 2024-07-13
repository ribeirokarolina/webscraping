import csv
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

#open browser
navegador = webdriver.Chrome('https://finance.yahoo.com/screener/new')
sleep(5)

#select region
select_region = navegador.find_element_by_class_name('Bd(0) H(28px) Bgc($lv3BgColor) C($primaryColor) W(100%) Fz(s) Pstart(28px)')
select_region.find_element_by_class_name('Ta(c) Pos(r) Va(tb) Pend(10px)')
sleep(4)

#click the button
button = select_region.find_element_by_xpath('//button[contains(text(),"Find Stocks")]')
button.click()
sleep(4)

#returns website information
site = BeautifulSoup(navegador.page_source, 'html.parser')
print(site.prettify())

#get the uploaded information
information = navegador.find_element_by_class_name('simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($hoverBgColor) ', href=True)
select_information = information[:3]

#saves information in csv format
csv = [information.text for information in select_information]

with open('caseCrawler.csv', 'w') as file:
    save = csv.save(file)
    for item in csv:
        save.writerow([item])



