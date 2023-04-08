set imgSize=-1
set source=--source VehicleR
set weights=--weights ./main/weights/singleclass.pt 
set output=--project ./main/output/
set name=--name detect --save-txt --max-det 40
set line_thickness=--line-thickness 2 --update
@REM set codes = '#--visualize' 

python ./main/yolov5/detect.py %source% %weights% %output% %line_thickness% %name%
