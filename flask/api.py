from flask import Flask
import time
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app, support_credentials=True)


@app.route('/image')
@cross_origin(supports_credentials=True)
def get_images():
    return {'image': ["image1", "image2", "image3"]}


@app.route('/')
@cross_origin(supports_credentials=True)
def server():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()