import os

from fastapi import (
    FastAPI, Form, File, 
    UploadFile, Request, HTTPException
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated

from utils.errorHandler import handleError
from classifier import classify
from preprocessor import preprocess

APP = FastAPI()
APP.mount("/static", StaticFiles(directory="public", html=True), name="public" )

def public_asset(asset_path: str):
    PUBLIC_PATH = os.path.join(".", "public")
    return os.path.join(PUBLIC_PATH, asset_path);

@APP.get("/")
async def index():
    return FileResponse(public_asset("index.html"));


@APP.post("/predict")
async def predict(image: Annotated[UploadFile, Form()]):
    err = {};

    if(image.size == 0): err["detail"] = "no_image"
    
    isInvalidRequest = len(err.keys()) > 0
    if isInvalidRequest:
        raise HTTPException(
            **handleError(err)
        )

    img = await image.read()
    prediction = classify(preprocess(img))

    return {
        "detail": "success",
        "prediction": prediction
    }

