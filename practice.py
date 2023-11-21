import requests
from bs4 import BeautifulSoup

url = "https://www.python.org"

res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.text,features="lxml")

for h2 in soup.find_all("h2"):
    print(h2.text)

li = [to_h2_list.text for to_h2_list in soup.find_all("h2")]



# for to_h2_list in soup.find_all("h2"): リスト内包表記の元
#     li.append(to_h2_list.text)

print(li)