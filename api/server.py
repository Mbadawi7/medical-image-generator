from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import io
from PIL import Image
from api.model_adapter import ImageGenerator
from api.dicom_utils import to_dicom

app = FastAPI(title="Medical Image Generator API", version="1.0")

generator = ImageGenerator()

class GenerateRequest(BaseModel):
    seed: int | None = None
    width: int = 128
    height: int = 128

@app.get("/healthz")
def healthz():
    return {"status": "healthy"}

@app.post("/generate")
def generate_image(req: GenerateRequest):
    img = generator.generate_image(req.seed, (req.height, req.width))
    pil = Image.fromarray(img)
    buf = io.BytesIO()
    pil.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

@app.post("/generate_dicom")
def generate_dicom(req: GenerateRequest):
    img = generator.generate_image(req.seed, (req.height, req.width))
    dicom_path = to_dicom(img)
    return FileResponse(dicom_path, media_type="application/dicom")

@app.get("/")
def root():
    return {"message": "Use /generate or /generate_dicom endpoints."}
