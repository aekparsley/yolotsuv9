from ultralytics import YOLO
model = YOLO(r"F:\Programming\Pycod\yolotsuv9\ultralytics\cfg\models\v9\yolov9c.yaml")
model.info()
model.train(r"F:\Programming\Pycod\yolotsuv9\ultralytics\cfg\data\coco128.yaml")