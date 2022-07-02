import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {token}'}
        params = {'path': f'{file_name}',
                  'overwrite': 'true'}

        # Получение ссылки на загрузку
        response = requests.get(url=url, headers=headers, params=params)
        href = response.json().get('href')

        # Загрузка файла
        uploader = requests.put(href, data=open(file_path, 'rb'))


if __name__ == '__main__':
    file_path = str(input('Введите путь к файлу, который хотите сохранить: '))
    file_name = file_path.replace('\\', '/').split('/')[-1]
    token = str(input('Введите ваш токен: '))

    uploader = YaUploader(token)
    result = uploader.upload(file_path)