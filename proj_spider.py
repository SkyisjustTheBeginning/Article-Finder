import scrapy
import requests
from bs4 import BeautifulSoup
urls=[]
r = requests.get('https://thehackernews.com/')
soup = BeautifulSoup(r.content, "lxml")
for link in soup.findAll('a'):
    i = link.get('href')
    if 'https://thehackernews.com/2023/' in i:
        urls.append(i)
keywords = ['Blind Eagle','Microsoft','Spyware','Russian']
pref_author = 'Ravie Lakshmanan'
class ProjectSpider(scrapy.Spider):
    name = "project"
    start_urls=urls
    def parse(self, response):
        text = ''.join(response.css('p::text').getall())
        author = response.css('span.author::text').get()
        for key in keywords:
            if key.upper() in text.upper():
                self.log('Article Found with Keywords')
                with open('/home/computer/urls.txt','a') as handle:
                    handle.write(str(response.url))
                    handle.write('\n')
            elif pref_author.upper() == str(author).upper():
                self.log('Article Found from Author')
                with open('/home/computer/urls.txt','a') as handle:
                    handle.write(str(response.url))
                    handle.write('\n')