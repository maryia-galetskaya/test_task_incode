import os
import mediapipe as mp

model_path = 'pose_landmarker_heavy.task'

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE
)

def get_detector():
    try:
        detector = PoseLandmarker.create_from_options(options)
    except Exception as e:
        raise RuntimeError(f"Failed to create the PoseLandmarker detector: {e}")
    return detector

def get_landmarks_from_file(file_path: str):
    """
    Create landmarks from the image file.
    """
    try:
        mp_image = mp.Image.create_from_file(file_path)
        detector = get_detector()
        detection_result = detector.detect(mp_image)
        if not detection_result.pose_landmarks:
            raise ValueError("No pose landmarks detected in the image")
        return detection_result.pose_landmarks[0]
    except Exception as e:
        raise ValueError(f"Failed to prepare file for processing: {e}")

def are_hands_above(landmarks) -> bool:
    """
    Check if both hands are above the head based on the pose landmarks.
    """
    relevant_hand_parts = [
        landmarks[15], landmarks[16],  # Wrists
        landmarks[17], landmarks[18],  # Pinkies
        landmarks[19], landmarks[20],  # Index fingers
        landmarks[21], landmarks[22]   # Thumbs
    ]

    relevant_head_parts = [
        landmarks[7], landmarks[8],  # Ears
        landmarks[2], landmarks[5]   # Eyes
    ]
    
    head_y_values = [part.y for part in relevant_head_parts]

    for part in relevant_hand_parts:
        if part.y > min(head_y_values):
            return False
    
    return True
