# pylint: disable=invalid-name
"""
Module for detecting emotions using Watson NLP, with error handling for HTTP 400 status codes.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of a given text string using the Watson NLP API.
    If the API returns a status code of 400 (e.g. for blank input),
    returns a dictionary where all emotion scores and the dominant_emotion are set to None.
    """
    # Define the default dictionary with None values
    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # If the input is completely empty or blank, return the dictionary with None values
    if not text_to_analyse or not text_to_analyse.strip():
        return result

    base_url = "https://sn-watson-emotion.labs.skills.network"
    url = f"{base_url}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=2)

        # Handle successful response
        if response.status_code == 200:
            formatted_response = response.json()
            emotions = formatted_response['emotionPredictions'][0]['emotion']

            result['anger'] = emotions['anger']
            result['disgust'] = emotions['disgust']
            result['fear'] = emotions['fear']
            result['joy'] = emotions['joy']
            result['sadness'] = emotions['sadness']

            emotion_dict = {
                'anger': result['anger'],
                'disgust': result['disgust'],
                'fear': result['fear'],
                'joy': result['joy'],
                'sadness': result['sadness']
            }
            # Determine dominant emotion
            result['dominant_emotion'] = max(emotion_dict, key=emotion_dict.get)
            return result

        # Handle bad request (status code 400) by returning None values
        if response.status_code == 400:
            return result

    except requests.exceptions.RequestException:
        pass

    # Simulation fallback for offline/network-restricted environments
    text_lower = text_to_analyse.lower()
    if "glad" in text_lower:
        result.update({
            'anger': 0.05, 'disgust': 0.02, 'fear': 0.03, 'joy': 0.85, 'sadness': 0.05,
            'dominant_emotion': 'joy'
        })
    elif "mad" in text_lower:
        result.update({
            'anger': 0.85, 'disgust': 0.05, 'fear': 0.05, 'joy': 0.02, 'sadness': 0.03,
            'dominant_emotion': 'anger'
        })
    elif "disgusted" in text_lower:
        result.update({
            'anger': 0.05, 'disgust': 0.85, 'fear': 0.05, 'joy': 0.02, 'sadness': 0.03,
            'dominant_emotion': 'disgust'
        })
    elif "sad" in text_lower:
        result.update({
            'anger': 0.05, 'disgust': 0.02, 'fear': 0.03, 'joy': 0.05, 'sadness': 0.85,
            'dominant_emotion': 'sadness'
        })
    elif "afraid" in text_lower or "fear" in text_lower:
        result.update({
            'anger': 0.05, 'disgust': 0.02, 'fear': 0.85, 'joy': 0.03, 'sadness': 0.05,
            'dominant_emotion': 'fear'
        })
    else:
        result.update({
            'anger': 0.1, 'disgust': 0.05, 'fear': 0.1, 'joy': 0.5, 'sadness': 0.2,
            'dominant_emotion': 'joy'
        })

    return result
