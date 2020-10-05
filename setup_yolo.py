from ImageProcess import ImageProcess
import imutils
import os
import progressbar
from pwn import log

# set the paths for the YOLO weights, cfg file, COCO names file
def Setup(yolo_path, cv2):
	weights = os.path.sep.join([yolo_path, "yolov3.weights"])
	labelsPath = os.path.sep.join([yolo_path, "coco.names"])
	configuration = os.path.sep.join([yolo_path, "yolov3.cfg"])
	labels = open(labelsPath).read().strip().split("\n")
	# load the saved weights into the network  
	net = cv2.dnn.readNetFromDarknet(configuration, weights)
	# extract the list of all layers
	ln = net.getLayerNames()
	ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
	return net, ln, labels

def detect_and_write(yolo, opname, cap, frameno, create, cv2):
	try:
		# show the progress 
		total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		bar = progressbar.ProgressBar(maxval=total_frames, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
		log.info("Starting the proccessing of the video, it may take time depending on the length of the video")
		bar.start()
		while(True):
			# get next frame
			ret, frame = cap.read()
			if not ret:
				break
			current_img = frame.copy()
			current_img = imutils.resize(current_img, width=480)
			video = current_img.shape
			frameno += 1
			bar.update(frameno)
			if(frameno%2 == 0 or frameno == 1):
				net, ln, labels = Setup(yolo, cv2)
				processedImg = ImageProcess(current_img, net, ln, labels, cv2)
				Frame = processedImg
				# show the modified frame
				#cv2.imshow("Image", Frame)
				if create is None:
					fourcc = cv2.VideoWriter_fourcc(*'XVID')
					create = cv2.VideoWriter(opname, fourcc, 30, (Frame.shape[1], Frame.shape[0]), True)
			# write frame to output video
			create.write(Frame)
			if cv2.waitKey(1) & 0xFF == ord('s'):
				break
		bar.finish()
	except KeyboardInterrupt:
		log.warn('Interrupted')
		exit(0)