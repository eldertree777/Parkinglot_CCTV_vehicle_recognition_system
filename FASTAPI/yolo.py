import torch
import cv2
import os
class vehicle_recognition:
    def __init__(self):
        #init setting
        os.chdir("D:\code\Parkinglot_CCTV_vehicle_recognition_system\YOLO\yolov5")

        # Model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

        # Images
        self.imgPath = 'D:\code\YOLO\dataset\img\\'  # or file, Path, PIL, OpenCV, numpy, list
        
        

    def setImgPath(self, filename):
        self.imgPath = 'D:\code\YOLO\dataset\img\\'
        self.imgPath += filename
        #self.img = cv2.imread(self.imgPath)[..., ::-1] # Pre-processing OpenCV image (BGR to RGB)
        return self.imgPath
    
    def makeModel(self):
         # Inference
        self.results = self.model(self.imgPath)

    def printResult(self):
        # Results
        self.results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

    def howManyCar(self):
        count = 0
        for i in range(len(self.results.pred[0])):
            if((self.results.pred[0][i][-1] == 2) | (self.results.pred[0][i][-1] == 7) ):
                count+=1
        
        return count

