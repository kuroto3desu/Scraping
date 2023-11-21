import requests
from bs4 import BeautifulSoup


url = "https://www.python.org"

res = requests.get(url)
result = res.status_code
if result == 200:
    print("接続に成功しました")
elif result != 200:
    print("接続に失敗しました")

tx = res.text
soup = BeautifulSoup(tx, features="lxml")
print(soup.h2.text)