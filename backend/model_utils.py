import tensorflow as tf
import numpy as np
from PIL import Image

CLASS_NAMES = ['Black_Sigatoka', 'Fusarium_Wilt', 'Healthy', 'Not_Banana_Leaf']  # must match training order exactly

def load_model():
    return tf.keras.models.load_model('models/unified_best_model.keras')

def predict(model, file):
    img = Image.open(file).convert('RGB').resize((224, 224))
    arr = np.array(img)
    arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)
    arr = np.expand_dims(arr, axis=0)

    preds = model.predict(arr)[0]
    idx = np.argmax(preds)
    predicted_class = CLASS_NAMES[idx]
    confidence = float(preds[idx])

    if predicted_class == 'Not_Banana_Leaf':
        return {
            'is_banana_leaf': False,
            'message': "This doesn't look like a banana leaf. Please upload a clear photo of a banana leaf for analysis."
        }

    return {
        'is_banana_leaf': True,
        'class': predicted_class,
        'confidence': round(confidence * 100, 2)
    }