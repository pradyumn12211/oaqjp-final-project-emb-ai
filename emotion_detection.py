import requests

def emotion_detector(text_to_analyze):
   
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }

    # POST request to  Watson NLP library
    response = requests.post(url, headers=headers, json=input_json)

    
    return response.text


if __name__ == "__main__":
    test_text = "I love this new technology."
    print(emotion_detector(test_text))
