from flask import Flask, request, jsonify
from model_utils import load_model, predict
from recommendations import RECOMMENDATIONS

app = Flask(__name__)
model = load_model()

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    result = predict(model, request.files['image'])

    if not result['is_banana_leaf']:
        return jsonify({'valid': False, 'message': result['message']})

    recommendation = RECOMMENDATIONS.get(result['class'], {})
    return jsonify({
        'valid': True,
        'class': result['class'],
        'confidence': result['confidence'],
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)