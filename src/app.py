import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

APP = FastAPI()
APP.mount("/static", StaticFiles(directory="public", html=True), name="public" )

def public_asset(asset_path: str):
    PUBLIC_PATH = os.path.join(".", "public")
    return os.path.join(PUBLIC_PATH, asset_path);

@APP.get("/")
async def index():
    return FileResponse(public_asset("index.html"));

@APP.post("/predict")
async def predict(request: Request):
    request = await request.form()
    err = {};

    if "chocoImage" in request.keys():
        image = request["chocoImage"]
        if(image.size == 0):
            err["status_code"] = 400
            err["detail"] = "no_image"
    
    isInvalidRequest = len(err.keys()) > 0
    if isInvalidRequest:
        raise HTTPException(
            status_code=err["status_code"], 
            detail=err["detail"]
        )

    return {
        "detail": "success",
        "prediction": ""
    }

