import os
from utils.pose_operations import get_landmarks_from_file, are_hands_above

def test_get_landmarks_from_file():
    test_image_path = "tests/test_image.jpg"

    assert os.path.exists(test_image_path), "Test image not found."

    landmarks = get_landmarks_from_file(test_image_path)
    
    assert landmarks, "No landmarks detected."
    assert len(landmarks) > 0, "Landmarks list is empty."

def test_are_hands_above():
    class Landmark:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
    
    landmarks = [Landmark(0, 0.1, 0) for _ in range(33)]

    landmarks[7].y = landmarks[8].y = 0.5   # Ears
    landmarks[2].y = landmarks[5].y = 0.5   # Eyes

    landmarks[15].y = landmarks[16].y = 0.1  # Wrists
    landmarks[17].y = landmarks[18].y = 0.1  # Pinkies
    landmarks[19].y = landmarks[20].y = 0.1 # Index fingers
    landmarks[21].y = landmarks[22].y = 0.1 # Thumbs

    result = are_hands_above(landmarks)
    
    assert result, "Hands above head detection failed."
