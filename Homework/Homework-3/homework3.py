import time
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

browser = webdriver.Chrome()


url = input("사이트 URL 입력 : ")

browser.get(url)
time.sleep(3)

page = browser.page_source

soup = BeautifulSoup(page, 'html.parser')
web_text = soup.get_text()
 
spwords=set(STOPWORDS)
spwords.add('바로가기')
spwords.add('자동완성')

wordcloud = WordCloud(font_path='C:\Windows\Fonts\HYGPRM.TTF', width=800, height=400, background_color='white', stopwords=spwords).generate(web_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

browser.quit()