import shutil
from fastapi import UploadFile
import os
from tempfile import NamedTemporaryFile

def save_file(file: UploadFile) -> str:
    """
    Save the uploaded file to a temporary location.
    """
    try:
        os.makedirs('media', exist_ok=True)
        
        file_location = f"media/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_location
    except Exception as e:
        raise ValueError(f"Failed to save the image file: {e}")

def delete_file(file_path: str):
    """
    Delete the temporary file.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        raise ValueError(f"Failed to delete the file: {e}")