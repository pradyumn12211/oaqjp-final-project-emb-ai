"""
server.py

This module sets up a Flask web server that provides an endpoint for analyzing emotions
from a given text statement. It uses the emotion_detector function from the EmotionDetection
package to get emotion predictions and returns a formatted response.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_route():
    """
    Handles POST requests to analyze emotions from the given statement.
    Expects JSON with a 'statement' key.
    """
    data = request.get_json()
    statement = data.get('statement')

    if not statement:
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
