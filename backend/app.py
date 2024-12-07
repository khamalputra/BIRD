from flask import Flask, jsonify, request
from google.cloud import vision
from google.oauth2 import service_account
import os
import firebase_admin
from firebase_admin import credentials, auth

# Set the path to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/khamalade/BIRD/backend/vision_api_key.json'

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/home/khamalade/BIRD/backend/firebase_key.json')
firebase_admin.initialize_app(cred)

# Example route to verify token
@app.route('/api/verify-token', methods=['POST'])
def verify_token():
    id_token = request.json.get('idToken')
    try:
        decoded_token = auth.verify_id_token(id_token)
        return jsonify({"message": "User authenticated", "user": decoded_token})
    except:
        return jsonify({"message": "Invalid token"}), 401

app = Flask(__name__)
client = vision.ImageAnnotatorClient()

@app.route('/api/analyze-image', methods=['POST'])
def analyze_image():
    file = request.files['image']
    content = file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    result = [label.description for label in labels]
    return jsonify({"labels": result})

if __name__ == '__main__':
    app.run(debug=True)