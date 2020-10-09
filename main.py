from setup_yolo import Setup
import cv2


main_bp = Blueprint('main', __name__)
main_api = Api(main_bp)


class Main(Resource):
    def get(self):
        create = None
        frameno = 0
        inp = "input"
        outp = "output.py"
        yolo = 'yolov3/'
        cap = cv2.VideoCapture(inp)
        ret, frame = cap.read()
        if not ret:
            break
        current_img = frame.copy()
        current_img = imutils.resize(current_img, width=480)
        video = current_img.shape
        frameno += 1
        if(frameno%2 == 0 or frameno == 1):
            net, ln, labels = Setup(yolo,cv2)
            processedImg = ImageProcess(current_img,net,ln,labels,cv2)
            Frame = processedImg
            if create is None:
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                create = cv2.VideoWriter(opname, fourcc, 30, (Frame.shape[1], Frame.shape[0]), True)
        #write frame to output video
        create.write(Frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

        return {"0":"1"}

