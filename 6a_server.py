"""
Flask web server for the Emotion Detection application.
Exposes endpoints for rendering the frontend and performing emotion detection analysis.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Endpoint to analyze text for emotions using Watson NLP.
    Retrieves the 'textToAnalyze' query parameter and returns a formatted result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Analyze the emotion of the input text
    response = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None, indicating blank/invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    # Format the success message
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Serves the main frontend index.html page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)