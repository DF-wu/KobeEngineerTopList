from selenium import webdriver
from bs4 import BeautifulSoup
import requests

pageSource = requests.get('https://kaobei.engineer/cards/show/1371')
# driver = webdriver.Chrome(executable_path=r'chromedriver')  #
# driver.get('https://kaobei.engineer/cards/show/1303')  # 輸入範例網址，交給瀏覽器 
# pageSource = driver.page_source  # 取得網頁原始碼
# print(pageSource)



tag =  'img[class = "rounded mx-auto d-block"]' #input("請輸入定位元素，class前面加上.，id前面加上# ")

soup = BeautifulSoup(pageSource.text, "lxml")

res = soup.select('{}'.format(tag))

src = soup.find("img",class_= "rounded mx-auto d-block")["src"]

print(len(src))
print(src)
# print (res)
# for drink in soup.select('{}'.format(tag)):
#     print(drink.get_text())
