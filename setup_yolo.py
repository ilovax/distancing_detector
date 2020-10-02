from ImageProcess import ImageProcess
import imutils
import os

#set the paths for the YOLO weights, cfg file, COCO names file
def Setup(yolo_path,cv2):
    weights = os.path.sep.join([yolo_path, "yolov3.weights"])
    labelsPath = os.path.sep.join([yolo_path, "coco.names"])
    configuration = os.path.sep.join([yolo_path, "yolov3.cfg"])
    labels = open(labelsPath).read().strip().split("\n")
    #load the saved weights into the network  
    net = cv2.dnn.readNetFromDarknet(configuration, weights)
    #extract the list of all layers
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return net, ln, labels

