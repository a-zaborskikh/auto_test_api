import json


class CheckingResponse:
    """Методы для проверки ответов запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус-кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-коды не совпадают'
        print(f'Проверка прошла успешно! Статус-код = {result.status_code} совпадает с ожидаемом результатом')

    @staticmethod
    def check_json_keys(result, expected_value):
        """Метод для проверки наличия ключей в ответе запроса"""
        keys = json.loads(result.text)    # Преобразовать строки json в словарь
        print(f'Ключи из ответа запроса: {list(keys)}')
        assert list(keys) == expected_value, 'ОШИБКА, Список ключей не совпадает в ответе запроса'
        print("Все ключи присутствуют в ответе запроса")

    @staticmethod
    def check_json_value(result, key, expected_value_key):
        """Метод для проверки значения обязательного ключа в ответе запроса"""
        all_keys = result.json()
        print(f'All keys: {all_keys}')
        json_value = all_keys.get(key)
        print(f'json_key: {json_value}')
        assert json_value == expected_value_key, (f'ОШИБКА, Значение ключа "{key} не соответствует'
                                                  f'ожидаемому результату "{expected_value_key}')
        print(f'УСПЕШНО! Значение ключа "{key}" соответствует ожидаемому результату')

    @staticmethod
    def check_json_search_word_in_value(result, key, search_word):
        """Метод для проверки значений ключей в ответе запроса при помощи поиска по определенному слову"""
        all_keys = result.json()
        json_value = all_keys.get(key)
        print(f'json_key: {json_value}')
        assert search_word in json_value
        print(f'Слово "{search_word}" присутствует в значении "{json_value}" ключа "{key}"')
