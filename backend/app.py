from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from normal_resnet import classify_with_normal_resnet
from optimized_resnet import classify_with_optimized_resnet

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)  # Allow cross-origin requests

UPLOAD_FOLDER = '../uploads/input_images/'
OUTPUT_FOLDER_1 = '../uploads/output_images_1/'
OUTPUT_FOLDER_2 = '../uploads/output_images_2/'

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

@app.route('/upload', methods=['POST'])
def upload_folder():
    create_directory_if_not_exists(UPLOAD_FOLDER)

    # Read model_type from request JSON data
    request_data = request.get_json()
    model_type = request_data.get('model_type')

    if not model_type:
        return jsonify({'error': 'Model type not specified'}), 400

    # Determine output folder based on model_type
    if model_type == 'preoptimized':
        output_folder = OUTPUT_FOLDER_1
    elif model_type == 'optimized':
        output_folder = OUTPUT_FOLDER_2
    else:
        return jsonify({'error': 'Invalid model type specified'}), 400

    # Perform classification based on model_type
    results = None
    if model_type == 'preoptimized':
        results = classify_with_normal_resnet(UPLOAD_FOLDER, output_folder)
    elif model_type == 'optimized':
        results = classify_with_optimized_resnet(UPLOAD_FOLDER, output_folder)

    return jsonify({'message': 'Images classified successfully', 'results': results}), 200

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
