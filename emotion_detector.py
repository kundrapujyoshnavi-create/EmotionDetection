def emotion_detector(text):

    emotions = {
        "anger": 0.05,
        "disgust": 0.02,
        "fear": 0.10,
        "joy": 0.80,
        "sadness": 0.03
    }

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions