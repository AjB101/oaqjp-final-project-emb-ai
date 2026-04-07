# # import requests

# # def sentiment_analyzer(text_to_analyse):
# # 	url =  "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
# # 	headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 
# # 	myobj = { "raw_document": { "text": text_to_analyse } }
# # 	response = requests.post(url, json = myobj, headers=header)
# # return response.text()


# import requests
# import json

# def emotion_detector(text_to_analyse):
#     url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
#     headers = {
#         "Content-Type": "application/json", 
#         "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
#     }

#     myobj = {
#         "raw_document": {
#             "text": text_to_analyse
#         }
#     }

#     response = requests.post(url, json=myobj, headers=headers)
#     # response = requests.post(
#     #     url,
#     #     data=json.dumps(myobj),   # ✅ KEY CHANGE (NOT json=)
#     #     headers=headers
#     # )
#     return response.text

# print(emotion_detector("I love this new technology."))


# import requests
# import json

# def emotion_detector(text_to_analyze):
#     url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
#     headers = {
#         "Content-Type": "application/json",
#         "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
#     }

#     input_json = {
#         "raw_document": {
#             "text": text_to_analyze
#         }
#     }

#     response = requests.post(url, data=json.dumps(input_json), headers=headers)

#     # Step 1: Convert response text → dictionary
#     response_dict = json.loads(response.text)

#     # Step 2: Extract emotions
#     emotions = response_dict["emotionPredictions"][0]["emotion"]

#     anger = emotions["anger"]
#     disgust = emotions["disgust"]
#     fear = emotions["fear"]
#     joy = emotions["joy"]
#     sadness = emotions["sadness"]

#     # Step 3: Find dominant emotion
#     dominant_emotion = max(emotions, key=emotions.get)

#     # Step 4: Return formatted output
#     return {
#         'anger': anger,
#         'disgust': disgust,
#         'fear': fear,
#         'joy': joy,
#         'sadness': sadness,
#         'dominant_emotion': dominant_emotion
#     }

# if __name__ == "__main__":
#     print(emotion_detector("I love this new technology"))



import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, data=json.dumps(input_json), headers=headers)

    # 🔥 ERROR HANDLING (Task requirement)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Normal processing
    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': dominant_emotion
    }

