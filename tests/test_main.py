import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_image():
    test_image_path = "tests/test_image.jpg"

    assert os.path.exists(test_image_path), "Test image not found."

    with open(test_image_path, "rb") as image_file:
        response = client.post(
            "/detect_hands/",
            files={"file": ("test_image.jpg", image_file, "image/jpeg")}
        )

    assert response.status_code == 200
    assert "hands_above_head" in response.json()
    assert isinstance(response.json()["hands_above_head"], bool)