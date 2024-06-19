from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from utils.file_operations import delete_file, save_file
from utils.pose_operations import are_hands_above, get_landmarks_from_file

app = FastAPI()

@app.post("/detect_hands/")
def upload_image(file: UploadFile = File(...)):
    valid_image_types = ["image/png", "image/jpeg", "image/jpg"]
    
    if file.content_type not in valid_image_types:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PNG, JPG, and JPEG files are allowed.")

    try:
        file_path = save_file(file)
        landmarks = get_landmarks_from_file(file_path)
        result = are_hands_above(landmarks)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred while processing the image.")
    finally:
        delete_file(file_path)

    return JSONResponse(content={"hands_above_head": result})

