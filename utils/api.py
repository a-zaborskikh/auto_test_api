from pprint import pprint

from utils.http_methods import HttpMethods

base_url = 'https://rahulshettyacademy.com'  # Базовая url
key = '?key=qaclick123'  # Параметр для всех запросов


class GoogleMapsApi:
    """Методы для тестирования Google maps API"""

    @staticmethod
    def create_new_place():
        """Метод для создания новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'  # Ресурс метода POST
        post_url = base_url + post_resource + key
        print(f'post_url: "{post_url}"')
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        pprint(result_post.json())
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""

        get_resource = '/maps/api/place/get/json'  # Ресурс метода GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(f'get_url: "{get_url}"')
        result_get = HttpMethods.get(get_url)
        pprint(result_get.json())
        return result_get

    @staticmethod
    def update_new_place(place_id):
        """Метод для изменения новой локации"""

        put_resource = '/maps/api/place/update/json'  # Ресурс метода PUT
        put_url = base_url + put_resource + key
        print(f'put_url: "{put_url}"')
        json_for_update_new_place = {
            "place_id": place_id,
            "address": "Friends address, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        pprint(result_put.json())
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления новой локации"""

        delete_resource = '/maps/api/place/delete/json'  # Ресурс метода DELETE
        delete_url = base_url + delete_resource + key
        print(f'delete_url: "{delete_url}"')
        print(place_id)
        json_for_delete_new_place = {
            "place_id": place_id,
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_place)
        pprint(result_delete.json())
        return result_delete
