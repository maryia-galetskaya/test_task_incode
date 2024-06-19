import os
from utils.file_operations import save_file, delete_file
from fastapi import UploadFile
from io import BytesIO

def test_save_file():
    file_content = b"dummy content"
    file = UploadFile(filename="test_file_image.jpg", file=BytesIO(file_content))

    file_path = save_file(file)
    
    assert os.path.exists(file_path), "File was not saved."

    with open(file_path, "rb") as f:
        saved_content = f.read()
        assert saved_content == file_content, "File content does not match."

    delete_file(file_path)

def test_delete_file():
    file_path = "media/test_delete_image.jpg"
    with open(file_path, "wb") as f:
        f.write(b"dummy content")

    assert os.path.exists(file_path), "File to delete does not exist."

    delete_file(file_path)
    
    assert not os.path.exists(file_path), "File was not deleted."