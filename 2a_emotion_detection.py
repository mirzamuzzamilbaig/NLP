# pylint: disable=invalid-name
"""
Emotion Detection module using Watson NLP API.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of a given text string using the Watson NLP API.
    Sends a POST request with the required headers and input text as a JSON object.
    Returns the raw response text from the API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    return response.text
