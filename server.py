from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    textToAnalyze = request.args.get("textToAnalyze")
    emotion_analysis_results = emotion_detector(textToAnalyze)
    result = "For the given statement, the system response is "
    result += str(emotion_analysis_results)[1:-1] + ". "
    result += f"The dominant emotion is {emotion_analysis_results['dominant_emotion']}."
    return result

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5001)