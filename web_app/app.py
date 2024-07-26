from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('custom_cnn_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image'].read()
    image = np.array(Image.open(io.BytesIO(image)).resize((512, 512)))
    image = image / 255.0  # Normalize
    predictions = model.predict(np.expand_dims(image, axis=0))
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
