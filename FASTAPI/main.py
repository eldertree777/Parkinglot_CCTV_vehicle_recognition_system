from typing import Optional
from yolo import vehicle_recognition
from fastapi import FastAPI
import os
from datetime import datetime


app = FastAPI()
model = vehicle_recognition()

# Hello World
@app.get("/")
def read_root():
    return {"Hello": "World"}

# getpath
@app.get("/getpath")
def read_root():
    os.chdir("D:\code\Parkinglot_CCTV_vehicle_recognition_system\YOLO\yolov5")
    path = os.getcwd()
    return {"Path": path}

# Hello items
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": model.setImgPath(q)}

#get_car_count
@app.get("/howManyCar/{imgPath}")
def read_item(item_id: int, q: Optional[str] = None):
    model.setImgPath(q)
    model.makeModel()
    value = model.howManyCar()
    return {"item_id": item_id, "q": value}

#get_car
@app.get("/howManyCar/")
def read_item():
    current_time = datetime.now()
    model.setImgPath('parkingLot16.PNG')
    model.makeModel()
    value = model.howManyCar()
    date = current_time.strftime("%Y-%m-%d-%H")
    return {"TIME": date, "LOC" : "NICO-1", "space": 40, "car" : value , "bus" : 0, "truck" : 2, "lastmile" : 0}


# @app.get("/items/{imgPath}")
# def read_item(imgPath: str):
#     model.setImgPath(imgPath)
#     model.makeModel()
#     value = model.howManyCar()
#     return {"car_number": value}

# uvicorn main:app --reload

