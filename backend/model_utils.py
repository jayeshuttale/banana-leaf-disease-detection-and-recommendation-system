import os
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
from PIL import Image

CLASS_NAMES = ['Black_Sigatoka', 'Fusarium_Wilt', 'Healthy', 'Not_Banana_Leaf']  # must match training order exactly

class RandomGaussianBlur(layers.Layer):
    """Applies Gaussian blur layer used during training/serialization."""
    def __init__(self, prob=0.3, **kwargs):
        super().__init__(**kwargs)
        self.prob = prob

    def call(self, images, training=None):
        if not training:
            return images
        apply_blur = tf.random.uniform([]) < self.prob
        def blur():
            kernel = tf.constant([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=tf.float32) / 16.0
            kernel = tf.reshape(kernel, [3, 3, 1, 1])
            kernel = tf.tile(kernel, [1, 1, 3, 1])
            return tf.nn.depthwise_conv2d(images, kernel, strides=[1, 1, 1, 1], padding='SAME')
        return tf.cond(apply_blur, blur, lambda: images)

    def get_config(self):
        config = super().get_config()
        config.update({"prob": self.prob})
        return config

def load_model():
    base_dir = os.path.dirname(__file__)
    model_candidates = [
        os.path.join(base_dir, 'models', 'unified_finetune_latest.keras'),
        os.path.join(base_dir, 'models', 'unified_best_model.keras'),
        os.path.join(base_dir, 'models', 'unified_baseline.keras'),
        os.path.join('models', 'unified_finetune_latest.keras'),
        os.path.join('models', 'unified_best_model.keras'),
        os.path.join('models', 'unified_baseline.keras')
    ]
    
    for candidate in model_candidates:
        if os.path.exists(candidate):
            return tf.keras.models.load_model(
                candidate,
                custom_objects={'RandomGaussianBlur': RandomGaussianBlur},
                compile=False
            )
            
    raise FileNotFoundError("Could not find model file in backend/models/")

def predict(model, file):
    img = Image.open(file).convert('RGB').resize((224, 224))
    # Pass raw [0, 255] float32 image because the Keras model already contains the preprocess_input layer
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)

    preds = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(preds))
    predicted_class = CLASS_NAMES[idx]
    confidence = float(preds[idx])

    if predicted_class == 'Not_Banana_Leaf':
        return {
            'is_banana_leaf': False,
            'confidence': round(confidence * 100, 2),
            'message': "This doesn't look like a banana leaf. Please upload a clear photo of a banana leaf for analysis."
        }

    return {
        'is_banana_leaf': True,
        'class': predicted_class,
        'confidence': round(confidence * 100, 2)
    }
