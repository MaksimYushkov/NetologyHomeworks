import requests
def main():
    class Character:

        def __init__(self, name):
            self.name = name

        def get_int_by_name(self, name):
            id = requests.get(f'{url}/search/{self.name}').json()['results'][0]['id']
            int = requests.get(f'{url}/{id}').json()
            return int['powerstats']['intelligence']

    url = 'https://superheroapi.com/api/2619421814940190'

    hulk = Character('Hulk')
    captain = Character('Captain America')
    thanos = Character('Thanos')

    char_int = {}
    char_int['Hulk'] = int(hulk.get_int_by_name('Hulk'))
    char_int['Captain America'] = int(captain.get_int_by_name('Captain America'))
    char_int['Thanos'] = int(thanos.get_int_by_name('Thanos'))
    print(char_int)

    for key, value in char_int.items():
        max_int = 0
        if value > max_int:
            max_int = value
    print(f'Максимальный интеллект у {key} - {max_int}')


if __name__ == '__main__':
    main()