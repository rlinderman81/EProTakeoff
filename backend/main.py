from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil, uuid, os

from detect import detect_lights

app = FastAPI(title="Lighting Takeoff MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_plan(file: UploadFile = File(...)):
    """Upload a plan (PDF/image), run detection, return count & boxes"""
    ext = os.path.splitext(file.filename)[-1].lower()
    tmp_name = f"{uuid.uuid4()}{ext}"
    save_path = os.path.join(UPLOAD_DIR, tmp_name)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run object detection
    results = detect_lights(save_path)

    return JSONResponse(results)