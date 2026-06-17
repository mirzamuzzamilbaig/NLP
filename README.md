# Final Project - IBM Watson NLP - Emotion Detector

**Repository Name:** oaqjp-final-project-emb-ai  
**Developer:** Mirza Muzammil  
**Course Final Project:** Developing AI Applications with Python and Flask

This repository contains the completed **Final Project** for the **Emotion Detector** application. The application utilizes a Watson NLP model (via Skills Network API) to analyze text and detect the dominant emotion along with scores for anger, disgust, fear, joy, and sadness.

## Project Structure

*   `EmotionDetection/`: Core package containing the emotion detection logic.
    *   `__init__.py`: Package initializer.
    *   `emotion_detection.py`: Module invoking the Watson NLP API with a local simulation fallback.
*   `static/mywebscript.js`: Handles frontend XMLHttpRequests and DOM updates.
*   `templates/index.html`: Main HTML user interface.
*   `server.py`: Flask backend hosting the application and handling errors gracefully.
*   `test_emotion_detection.py`: Unit test suite testing core emotional classifications.

## Features

1.  **Watson NLP Integration:** Analyzes input statements and yields emotion confidence metrics.
2.  **Web API Deployment:** Interactive user interface served using Flask.
3.  **Robust Error Handling:** Detects blank inputs and returns appropriate HTTP 400 messages to prevent runtime crashes.
4.  **Static Code Analysis:** Achieves a perfect 10/10 score in Pylint validation.
