from flask import Flask, render_template_string, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
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
    filename = data.get('image')[27:]
    original_image = cv2.imread('../public/examples/' + filename)

    grayed, blurred, pre_processed, result, card, zoom, value, symbol, original = CardRecognition.drawImage(original_image)
    
    cv2.imwrite(f"../public/results/original.jpg", original)

    pre_processed = cv2.resize(pre_processed, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    grayed = cv2.resize(grayed, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    blurred = cv2.resize(blurred, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/grayed.jpg", grayed)
    cv2.imwrite(f"../public/results/blurred.jpg", blurred)
    cv2.imwrite(f"../public/results/pre_process.jpg", pre_processed)

    card = cv2.resize(card, (card.shape[1], card.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/card.jpg", card)

    zoom = cv2.resize(zoom, (zoom.shape[1], zoom.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/zoom.jpg", zoom)

    value = cv2.resize(value, (value.shape[1], value.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/value.jpg", value)

    symbol = cv2.resize(symbol, (symbol.shape[1], symbol.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/symbol.jpg", symbol)

    result = cv2.resize(result, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/result.jpg", result)

    return {
        'success': True,
        'file': 'Received'
    }


@app.route('/user/upload', methods=['POST'])
@cross_origin()
def handle_form():
    files = request.files['file']
    npimg = np.fromfile(files, np.uint8)

    original_image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    grayed, blurred, pre_processed, result, card,zoom, value, symbol, img = CardRecognition.drawImage(original_image)

    cv2.imwrite(f"../public/results/original.jpg", img)

    pre_processed = cv2.resize(pre_processed, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    grayed = cv2.resize(grayed, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    blurred = cv2.resize(blurred, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/grayed.jpg", grayed)
    cv2.imwrite(f"../public/results/blurred.jpg", blurred)
    cv2.imwrite(f"../public/results/pre_process.jpg", pre_processed)

    card = cv2.resize(card, (card.shape[1], card.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/card.jpg", card)

    zoom = cv2.resize(zoom, (zoom.shape[1], zoom.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/zoom.jpg", zoom)

    value = cv2.resize(value, (value.shape[1], value.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/value.jpg", value)

    symbol = cv2.resize(symbol, (symbol.shape[1], symbol.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/symbol.jpg", symbol)

    result = cv2.resize(result, (original_image.shape[1], original_image.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/result.jpg", result)

    return {
        'success': True,
        'file': 'Received'
    }
