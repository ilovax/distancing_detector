import cv2
import sys
from setup_yolo import detect_and_write



if __name__ == '__main__':
	create = None
	frameno = 0
	if len(sys.argv) < 4:
		print("[-] Usage python distancing_detector.py input_video output_video yolo")
		exit(0)
	#inputs	
	inp = sys.argv[1]
	outp = sys.argv[2]
	yolo = sys.argv[3]

	cap = cv2.VideoCapture(inp)
	detect_and_write(yolo,outp,cap,frameno,create,cv2)
	print("Completed!")
	cap.release()
	cv2.destroyAllWindows()