from flask import Flask
import time
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/image')
@cross_origin(supports_credentials=True)
def get_images():
    return {'image': ["image1", "image2", "image3"]}