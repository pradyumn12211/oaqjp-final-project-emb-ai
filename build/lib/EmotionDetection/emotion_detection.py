import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if response.status_code == 200:
            emotion_predictions = response_data.get("emotionPredictions", [{}])
            if emotion_predictions and "emotion" in emotion_predictions[0]:
                emotions = emotion_predictions[0]["emotion"]
                anger_score = emotions.get("anger", 0)
                disgust_score = emotions.get("disgust", 0)
                fear_score = emotions.get("fear", 0)
                joy_score = emotions.get("joy", 0)
                sadness_score = emotions.get("sadness", 0)

                emotion_scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
                emotion_labels = ["anger", "disgust", "fear", "joy", "sadness"]
                dominant_emotion = emotion_labels[emotion_scores.index(max(emotion_scores))]

            else:
                anger_score = disgust_score = fear_score = joy_score = sadness_score = None
                dominant_emotion = None

        else:
            anger_score = disgust_score = fear_score = joy_score = sadness_score = None
            dominant_emotion = None

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

# Example usage
if __name__ == "__main__":
    text = "I am so happy I am doing this"
    result = emotion_detector(text)
    print(result)
