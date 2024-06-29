from datetime import date
from config import API_KEY
from tests.utils.create_client import client


class BookTests:

    def __init__(self, author_id: int):
        self.test_id = None

        self.author_id = author_id

        self.test_time = str(date.today())

        self.test_json = {
            "name": "test_book",
            "title": "test_book",
            "annotation": "test_book",
            "date_publishing": self.test_time,
            "author_id": self.author_id
        }

        self.test_json_with_id = None

    def test_create_book(self) -> None:
        response = client.post(
            "/books",
            headers={"api-key": API_KEY},
            json=self.test_json
        )

        assert response.status_code == 200

        self.test_id = response.json()["id"]
        print(self.test_id)
        self.test_json_with_id = {
            "id": self.test_id,
            "name": "test_book",
            "title": "test_book",
            "annotation": "test_book",
            "date_publishing": self.test_time,
            "author_id": self.author_id
        }

        assert response.json() == self.test_json_with_id

    def test_read_book(self) -> None:
        response = client.get(f"/books/{self.test_id}", headers={"api-key": API_KEY}, )

        assert response.status_code == 200

        assert response.json() == self.test_json_with_id

    def test_read_books(self) -> None:
        response = client.get("/books", headers={"api-key": API_KEY})

        assert response.status_code == 200

        for i in response.json():
            if i == self.test_json_with_id:
                return

        assert Exception("Test 'test_read_all' is not accepted.")

    def test_delete_book(self) -> None:
        response = client.delete(f"/books/{self.test_id}", headers={"api-key": API_KEY})

        assert response.status_code == 200

        assert response.json() == self.test_json_with_id

    def test_read_deleted_book(self):
        response = client.get(f"/books/{self.test_id}", headers={"api-key": API_KEY})

        assert response.status_code == 404
