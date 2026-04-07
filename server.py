"""
Flask server for Emotion Detection application.
Handles routing, user input, and response formatting.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the homepage.

    Returns:
        HTML page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detect():
    """
    Analyze user input text and return emotion detection results.

    Returns:
        str: Formatted response or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle empty input
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    # Handle API error
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
