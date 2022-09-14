import requests
from bs4 import BeautifulSoup
import re
from scrapping.data import KEYWORDS, headers


def scrap_habr():
    response = requests.get('https://habr.com/ru/all/', headers=headers)
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')

    all_data = {}
    i = 1
    for article in articles:
        title = article.find('a', class_='tm-article-snippet__title-link').text.lower()

        pub_date = article.find('span', class_='tm-article-snippet__datetime-published').find('time').get('datetime') \
            [:10].lower()

        href = 'https://habr.com' + article.find('a', class_='tm-article-snippet__title-link').get('href').lower()

        description = article.find('div', class_='tm-article-body tm-article-snippet__lead')
        if 'article-formatted-body_version-2' in str(description):
            description_text = description.find('p').text.strip().lower()
        else:
            description_text = re.sub(r"^\s+|\n|\r|\s+$", '', re.sub(r"\s*Читать дальше.?.?", '', \
                                                                     description.text.strip())).lower()

        user_info = article.find('span', class_='tm-user-info__user').text.strip().lower()

        tags = article.find('div', class_='tm-article-snippet__hubs').text.lower()
        all_data[i] = [title, pub_date, href, description_text, user_info, tags]
        i += 1
    return all_data


def search_pub_by_keywords(all_data):
    list_ = []
    for values in all_data.values():
        for value in values:
            if any(element.lower() in value for element in KEYWORDS):
                list_.append(str(values[1]) + ' - ' + str(values[0] + ' - ' + str(values[2])))
    for el in set(list_):
        print(el)


def main():
    data = scrap_habr()
    search_pub_by_keywords(data)


if __name__ == '__main__':
    main()
