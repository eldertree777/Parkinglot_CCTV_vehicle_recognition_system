from typing import Optional
from yolo import vehicle_recognition
from fastapi import FastAPI
import os

app = FastAPI()
model = vehicle_recognition()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getpath")
def read_root():
    os.chdir("D:\code\Parkinglot_CCTV_vehicle_recognition_system\YOLO\yolov5")
    path = os.getcwd()
    return {"Path": path}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": model.setImgPath(q)}

@app.get("/howManyCar/{imgPath}")
def read_item(item_id: int, q: Optional[str] = None):
    model.setImgPath(q)
    model.makeModel()
    value = model.howManyCar()
    return {"item_id": item_id, "q": value}


# @app.get("/items/{imgPath}")
# def read_item(imgPath: str):
#     model.setImgPath(imgPath)
#     model.makeModel()
#     value = model.howManyCar()
#     return {"car_number": value}

# uvicorn main:app --reload