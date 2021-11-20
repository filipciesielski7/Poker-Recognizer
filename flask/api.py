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
    image = {'filename': data.get('image')}
    filename = data.get('image')[27:]

    original = cv2.imread('../public/examples/' + filename)

    cv2.imwrite(f"../public/results/original.jpg", original)

    grayed, blurred, pre_processed, przerobionyObraz, card,przyblizenie, gorna_czesc, dolna_czesc = CardRecognition.drawImage(original)

    pre_processed = cv2.resize(pre_processed, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    grayed = cv2.resize(grayed, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    blurred = cv2.resize(blurred, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/grayed.jpg", grayed)
    cv2.imwrite(f"../public/results/blurred.jpg", blurred)
    cv2.imwrite(f"../public/results/pre_process.jpg", pre_processed)

    card = cv2.resize(card, (card.shape[1], card.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/card.jpg", card)

    przyblizenie = cv2.resize(przyblizenie, (przyblizenie.shape[1], przyblizenie.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/zoom.jpg", przyblizenie)

    gorna_czesc = cv2.resize(gorna_czesc, (gorna_czesc.shape[1], gorna_czesc.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/value.jpg", gorna_czesc)

    dolna_czesc = cv2.resize(dolna_czesc, (dolna_czesc.shape[1], dolna_czesc.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/symbol.jpg", dolna_czesc)

    przerobionyObraz = cv2.resize(przerobionyObraz, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/result.jpg", przerobionyObraz)

    return {
        'success': True,
        'file': 'Received'
    }


@app.route('/user/upload', methods=['POST'])
@cross_origin()
def handle_form():
    files = request.files['file']
    npimg = np.fromfile(files, np.uint8)

    original = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    cv2.imwrite(f"../public/results/original.jpg", original)
    grayed, blurred, pre_processed, przerobionyObraz, card,przyblizenie, gorna_czesc, dolna_czesc = CardRecognition.drawImage(original)

    pre_processed = cv2.resize(pre_processed, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    grayed = cv2.resize(grayed, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    blurred = cv2.resize(blurred, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/grayed.jpg", grayed)
    cv2.imwrite(f"../public/results/blurred.jpg", blurred)
    cv2.imwrite(f"../public/results/pre_process.jpg", pre_processed)

    card = cv2.resize(card, (card.shape[1], card.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/card.jpg", card)

    przyblizenie = cv2.resize(przyblizenie, (przyblizenie.shape[1], przyblizenie.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/zoom.jpg", przyblizenie)

    gorna_czesc = cv2.resize(gorna_czesc, (gorna_czesc.shape[1], gorna_czesc.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/value.jpg", gorna_czesc)

    dolna_czesc = cv2.resize(dolna_czesc, (dolna_czesc.shape[1], dolna_czesc.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/symbol.jpg", dolna_czesc)

    przerobionyObraz = cv2.resize(przerobionyObraz, (original.shape[1], original.shape[0]), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(f"../public/results/result.jpg", przerobionyObraz)

    return {
        'success': True,
        'file': 'Received'
    }
