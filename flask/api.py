from flask import Flask, render_template_string, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import cv2
from skimage import io, data, filters, color, measure, exposure, morphology, img_as_float32
import numpy as np
from matplotlib import pyplot as plt
import threading
import CardRecognition

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/image', methods=["GET"])
@cross_origin()
def get_images():
    return {'image': ["image1", "image2", "image3"]}


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    data = request.get_json(silent=True)
    image = {'filename': data.get('image')}
    filename = data.get('image')[27:]

    original = cv2.imread('../public/examples/' + filename)
    cv2.imwrite(f"../public/original.jpg", original)

    przerobionyObraz = CardRecognition.drawImage(filename)
    cv2.imwrite(f"../public/result.jpg", przerobionyObraz)

    return {
        'success': True,
        'file': 'Received'
    }


@app.route('/user/upload', methods=['POST'])
@cross_origin()
def handle_form():
    files = request.files['file']
    npimg = np.fromfile(files, np.uint8)

    img1 = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.imwrite(f"../public/original.jpg", img1)

    img2 = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"../public/result.jpg", img2)
    
    return {
        'success': True,
        'file': 'Received'
    }