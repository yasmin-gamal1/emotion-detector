from functools import reduce
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_ = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=json_, headers=header,)
    formatted_response = json.loads(response.text)    

    return_value = formatted_response['emotionPredictions'][0]['emotion']
    return_value.update(
        {'dominant_emotion': reduce(lambda a, b: a if return_value[a] > return_value[b] else b, return_value)}
    )

    return return_value
