set imgSize=-1
set source=--source Vehicles
set weights=--weights ./main/weights/presinglecls.pt 
set output=--project ./output/
set name=--name detect --save-txt --max-det 40
set line_thickness=--line-thickness 2
@REM set codes = '#--visualize' 

python ./main/yolov5/detect.py %source% %weights% %output% %line_thickness% %name%
