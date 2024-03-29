from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

url = input()


def load_data(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    reviews = soup.find_all('p')
    reviews_clean = []
    for review in reviews:
        reviews_clean.append(review.find_all(string=True))

    users = soup.find_all('blockquote')
    users_clean = []
    for user in users:
        users_clean.append(user.find_all(string=True)[1])

    return reviews_clean, users_clean


#результат можно оформить в виде таблицы, в первом столбце будут находится имена пользователей, во втором - текст непосредственно самого отзыва и т.д.
data = load_data(url)
result = {}
for user in data[1]:
    result[user] = data[0][data[0].index([user]) + 1][0]
#print(result)
print(tabulate(result.items(), headers=['NAME', 'VALUE'], tablefmt="grid"))
