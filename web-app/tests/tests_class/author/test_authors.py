from datetime import date
from config import API_KEY
from tests.utils.create_client import client


class AuthorTests:

    def __init__(self):
        self.test_id = None

        self.test_time = str(date.today())

        self.test_json = {
            "first_name": "test_author",
            "last_name": "test_author",
            "date_birth": self.test_time,
            "biography": "test_author"
        }

        self.test_json_with_id = None

    def test_create_author(self) -> None:
        response = client.post(
            "/authors",
            headers={"api-key": API_KEY},
            json=self.test_json
        )

        assert response.status_code == 200

        self.test_id = response.json()["id"]

        self.test_json_with_id = {
            "id": self.test_id,
            "first_name": "test_author",
            "last_name": "test_author",
            "date_birth": self.test_time,
            "biography": "test_author"
        }

        assert response.json() == self.test_json_with_id

    def test_read_author(self) -> None:
        response = client.get(f"/authors/{self.test_id}", headers={"api-key": API_KEY})

        assert response.status_code == 200

        assert response.json() == self.test_json_with_id

    def test_read_authors(self) -> None:
        response = client.get("/authors", headers={"api-key": API_KEY})

        assert response.status_code == 200

        for i in response.json():
            if i == self.test_json_with_id:
                return

        assert Exception("Test 'test_read_all' is not accepted.")

    def test_delete_author(self) -> None:
        response = client.delete(f"/authors/{self.test_id}", headers={"api-key": API_KEY})

        assert response.status_code == 200

        assert response.json() == self.test_json_with_id

    def test_read_deleted_authors(self):
        response = client.get(f"/authors/{self.test_id}", headers={"api-key": API_KEY})

        assert response.status_code == 404
