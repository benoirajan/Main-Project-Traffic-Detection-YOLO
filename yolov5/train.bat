set imgSize=--img 640 
set batch=--batch -1 
set epochs=--epochs 3
set data=--data ./singlecls_ds/vehicle.yaml
set weights= 
@REM --weights ./main/yolov5/yolov5s.pt 
set name=--name pretrained_5s 
set code=--patience 30 --project ./main/train
@REM  --cfg ./main/yolov5/models/yolov5s.yaml 


python ./main/yolov5/train.py %imgSize% %batch% %epochs% %data% %weights% %name% %code%