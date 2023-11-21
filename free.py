import requests
from bs4 import BeautifulSoup

url = "https://tech-diary.net/python-scraping-books/"

res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.text,features="lxml")
article = soup.find("article").find_all(["h2","h3"])
toExtract = soup.find_all("h2",class_="l-articleBottom__title c-secTitle")
#print(article) #取得タグ確認用

for tag in toExtract:
        tag.extract()
 
article = soup.find("article").find_all(["h2","h3"])
li = [tag.text for tag in article]


# for h2 in soup.find_all("h2"):
#     print(h2.text)

# li = [to_h2_list.text for to_h2_list in soup.find_all("h2")]



print(li)