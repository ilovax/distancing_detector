from flask import Flask, render_template, request, send_file, redirect
from flask_restful import Resource, Api
from setup_yolo import detect_from_web_and_write 
import cv2

def detect(video):
	create = None
	frameno = 0
	inp = video 
	outp = video + "_out.avi"
	yolo = "yolov3/"
	cap = cv2.VideoCapture(inp)
	detect_from_web_and_write(yolo,outp,cap,frameno,create,cv2)
	cap.release()
	return outp
class Ping(Resource):
	def get(self):
		return {'ping': 'pong'}


def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	api = Api(app)
	api.add_resource(Ping, '/ping')
	@app.route('/', methods=['GET'])
	def main():
		return render_template("main.html")

	@app.route('/upload', methods=['POST'])
	def upload():
		vid = request.files['video']
		if vid.filename != '':
			vid.save(vid.filename)
			out_name = detect(vid.filename)
		return redirect('/show/{}'.format(out_name))
	
	@app.route('/show/<filename>', methods=['GET'])
	def download(filename):
		return render_template("download.html", filename=filename)

	@app.route('/video/<filename>')
	def get_video(filename):
		return	send_file(filename, attachment_filename=filename)
	

	return app
