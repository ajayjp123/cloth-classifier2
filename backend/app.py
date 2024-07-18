from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from normal_resnet import classify_with_normal_resnet
from optimized_resnet import classify_with_optimized_resnet

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)  # Allow cross-origin requests

UPLOAD_FOLDER = '../uploads/input_images/'
OUTPUT_FOLDER = '../uploads/output_images/'

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

@app.route('/upload', methods=['POST'])
def upload_folder():
    create_directory_if_not_exists(OUTPUT_FOLDER)

    input_folder = UPLOAD_FOLDER
    output_folder = OUTPUT_FOLDER

    model_type = request.form.get('model_type', 'preoptimized')

    if model_type == 'preoptimized':
        results = classify_with_normal_resnet(input_folder, output_folder)
    elif model_type == 'optimized':
        results = classify_with_optimized_resnet(input_folder, output_folder)
    else:
        return jsonify({'error': 'Invalid model type specified'}), 400

    return jsonify({'message': 'Images classified successfully', 'results': results}), 200

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
