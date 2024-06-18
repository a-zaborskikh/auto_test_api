from utils.api import GoogleMapsApi
from utils.checking import CheckingResponse


class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""

    def test_create_new_place(self):
        print('Метод POST')
        result_post = GoogleMapsApi.create_new_place()  # Вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get('place_id')  # Вернуть значение параметра place_id из ответа result_post
        print(f'Статус-код метода POST: {result_post.status_code}')
        expected_value_post = ['status', 'place_id', 'scope', 'reference', 'id']
        expected_key_post = 'status'
        expected_value_key_post = 'OK'
        CheckingResponse.check_status_code(result_post, 200)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_post, expected_value_post)
        CheckingResponse.check_json_value(result_post, expected_key_post, expected_value_key_post)

        print('Метод GET check POST')
        result_get = GoogleMapsApi.get_new_place(place_id)  # Вызов метода по проверке создания новой локации
        print(f'Статус-код метода GET check POST: {result_get.status_code}')
        expected_value_get = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        expected_key_get = 'accuracy'
        expected_value_key_get = '50'
        CheckingResponse.check_status_code(result_get, 200)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_get, expected_value_get)
        CheckingResponse.check_json_value(result_get, expected_key_get, expected_value_key_get)

        print('Метод PUT')
        result_put = GoogleMapsApi.update_new_place(place_id)  # Вызов метода по изменению создания новой локации
        print(f'Статус-код метода PUT: {result_put.status_code}')
        expected_value_put = ['msg']
        expected_key_put = 'msg'
        expected_value_key_put = 'Address successfully updated'
        CheckingResponse.check_status_code(result_put, 200)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_put, expected_value_put)
        CheckingResponse.check_json_value(result_put, expected_key_put, expected_value_key_put)

        print('Метод GET check PUT')
        result_get = GoogleMapsApi.get_new_place(place_id)  # Вызов метода по проверке изменения новой локации
        print(f'Статус-код метода GET check PUT: {result_get.status_code}')
        expected_value_get = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        expected_key_get = 'accuracy'
        expected_value_key_get = '50'
        CheckingResponse.check_status_code(result_get, 200)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_get, expected_value_get)
        CheckingResponse.check_json_value(result_get, expected_key_get, expected_value_key_get)

        print('Метод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # Вызов метода по удалению новой локации
        print(f'Статус-код метода DELETE: {result_delete.status_code}')
        expected_value_delete = ['status']
        expected_key_delete = 'status'
        expected_value_key_delete = 'OK'
        CheckingResponse.check_status_code(result_delete, 200)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_delete, expected_value_delete)
        CheckingResponse.check_json_value(result_delete, expected_key_delete, expected_value_key_delete)

        print('Метод GET check DELETE')
        result_get = GoogleMapsApi.get_new_place(place_id)  # Вызов метода по проверке удаления новой локации
        print(f'Статус-код метода GET check DELETE: {result_get.status_code}')
        expected_value_get = ['msg']
        expected_key_get = 'msg'
        search_word_check_delete = 'failed'
        CheckingResponse.check_status_code(result_get, 404)  # Вызов метода по проверке статус-кода
        CheckingResponse.check_json_keys(result_get, expected_value_get)
        CheckingResponse.check_json_search_word_in_value(result_get, expected_key_get, search_word_check_delete)

