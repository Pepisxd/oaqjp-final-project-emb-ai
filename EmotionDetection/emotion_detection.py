"""Emotion detection using the embedded Watson NLP EmotionPredict function."""

import json

import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Return the emotion scores and the dominant emotion of a given text.

    Sends text_to_analyze to the Watson NLP EmotionPredict function and formats
    the response as a dictionary holding anger, disgust, fear, joy and sadness
    scores plus the dominant emotion. Blank input makes the server answer with
    status code 400, in which case every value of the dictionary is None.
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None,
                'sadness': None, 'dominant_emotion': None}

    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    scores = {'anger': anger_score, 'disgust': disgust_score,
              'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dominant_emotion = max(scores, key=scores.get)

    return {'anger': anger_score, 'disgust': disgust_score,
            'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}
