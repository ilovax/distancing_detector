# Social-distancing-detector
Two interfaces:
    - Web interface
    - Terminal interface (using raspberry pi)

## 1-INTRODUCTION:

In this project we impliment a social distancing detector based on YOLO model for object detaction and split it into two parts:
### 1.1- Using web interface to upload a video and detect social distancing on it:
>Using flask framework and a smiple web page to upload a video and watch the results.

### 1.2- Using CLI :
>We can provide both the name of the input video and the output and must provide the yolo folder path.


## 2-Requirements:
- Requirements.txt contains the needed python libraries.
```bash
$ pip install -r requirements.txt 
```
- Download the yolo3 file:
-- https://github.com/tianhai123/yolov3/blob/master/cfg/coco.names
-- https://github.com/tianhai123/yolov3/blob/master/cfg/yolov3.cfg
-- https://pjreddie.com/media/files/yolov3.weights
- Move them to a folder
```bash
$ mkdir yolov3/
$ mv coco.name yolov3.cfg yolov3.weights yolov3/
```

## 3-Running the project
### 3.1 web server
```bash
$ flask run
```
>Then access  localhost:5000/ 
### 3.2 Cli 

```bash
$ python distancing_detector.py input_video output_video yolo_path
```
>yolo_path is the path to the directory with the yolov3 files (yolov3/).
you can enter 'cam' instead of the input_video for capturing from camera 
