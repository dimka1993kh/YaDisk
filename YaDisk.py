import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Запишем headers и params для GET запроса
        headers = {'Authorization' : self.token}
        params = {'path' : file_path, 'overwrite' : 'True'}
        # Выполним запрос, в котором получим ссылку на загрузку нашего файла
        resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params=params, headers=headers)
        # Проверка на успешность запроса
        if resp.status_code != 200:
            print('Незадача')
        # Получили ссылку для загрузки файла
        href = resp.json()['href']
        # Прочитаем файл на компьютере и отправим файл на диск
        with open(file_path, 'rb') as f:
            resp = requests.put(href, files={"file": f})
        if resp.status_code == 201:
            return f'Файл {file_path} успешно загружен'
        else:
            return 'Что-то пошло не так. Нет кода 201 (Успешная загрузка)'
         


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('wQb7_RJnatw.jpg')

