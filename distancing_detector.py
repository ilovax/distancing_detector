import cv2
import sys
from setup_yolo import detect_from_file_and_write, detect_from_cam_and_write
from pwn import log

def main():
	create = None
	frameno = 0
	if len(sys.argv) < 4:
		log.failure("Usage : python distancing_detector.py input_video output_video yolo_path")
		log.info("Use cam instead of input_video for capturing from camera")
		exit(0)
	#inputs	
	inp = sys.argv[1]
	outp = sys.argv[2]
	yolo = sys.argv[3]
	if inp == "cam":
		cap = cv2.VideoCapture(0)
		detect_from_cam_and_write(yolo,outp,cap,frameno,create,cv2)
	else:
		cap = cv2.VideoCapture(inp)
		detect_from_file_and_write(yolo,outp,cap,frameno,create,cv2)
	log.success("Completed!")
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()