import requests
from datetime import datetime, timedelta

date_now = datetime.now().date()
date_pass = date_now - timedelta(days=2)
url = f'https://api.stackexchange.com/2.3/search?fromdate={date_pass}&todate={date_now}&order=desc&sort=activity' \
      f'&tagged=Python&site=stackoverflow'

req = requests.get(url).json()
links_list = req['items']
for link in links_list:
    print(f"Ссылка: {link['link']}")
    print(f"Заголовок: {link['title']}")
