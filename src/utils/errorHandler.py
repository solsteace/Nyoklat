ERROR_LIST = {
    "no_image": {
        "status_code": 400, 
        "detail": "no_image"
    }
}

def handleError(err):
    return ERROR_LIST[err["detail"]]