from flask import Flask, render_template_string, request
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/image', methods=["GET"])
@cross_origin()
def get_images():
    return {'image': ["image1", "image2", "image3"]}


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    if request.method == 'POST':
        fs = request.files
        # fs = request.files.get('snap')
        if fs:
            fs.save('image.jpg')
            return 'Got Snap!'
        else:
            return 'You forgot Snap!'
    
    return 'Hello World!'