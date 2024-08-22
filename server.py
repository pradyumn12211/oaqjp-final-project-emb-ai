from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.get_json()
    statement = data.get('statement', '')

    result = emotion_detector(statement)

   
    emotions = ", ".join([f"'{key}': {value}" for key, value in result.items() if key != 'dominant_emotion'])
    dominant_emotion = result.get('dominant_emotion', '')

    response_message = (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return jsonify({
        'response_message': response_message,
        **result
    })

if __name__ == '__main__':
    app.run(debug=True)
