from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_apk():
    if 'apkFile' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400

    apk_file = request.files['apkFile']
    if apk_file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, apk_file.filename)
    apk_file.save(file_path)

    return jsonify({'message': f'APK cloned and saved as {apk_file.filename}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
