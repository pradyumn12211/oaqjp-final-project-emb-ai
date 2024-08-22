from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.json
    statement = data.get('statement', '')

    if not statement.strip():
        response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return jsonify(response), 400

    result = emotion_detector(statement)
    dominant_emotion = result.get('dominant_emotion')

    if dominant_emotion is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{dominant_emotion}."
    )
    return response_message

if __name__ == '__main__':
    app.run(debug=True)
