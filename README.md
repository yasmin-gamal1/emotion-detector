

---

# Emotion Detection App

This is a simple web application for detecting emotions in text using Python and Watson Natural Language Understanding (NLU) API.

## Files Included:

1. **emotion_detector.py**: Python script responsible for analyzing emotions in text using the Watson NLU API.
2. **server.py**: Flask server script that handles HTTP requests and serves the web application.
3. **test_emotion_detection.py**: Unit tests for the `emotion_detector.py` script to ensure its functionality.
4. **mywebscript.js**: JavaScript file containing client-side logic for interacting with the Flask server and handling text input.
5. **index.html**: HTML file for the web interface of the application.

## Getting Started:

1. **Installation**:
   - Clone this repository to your local machine.
   - Make sure you have Python installed on your system.

2. **Dependencies**:
   - Install the required Python packages by running:
     ```
     pip install -r requirements.txt
     ```
   - Ensure you have Flask installed. If not, install it using:
     ```
     pip install Flask
     ```

3. **Running the Application**:
   - Start the Flask server by executing:
     ```
     python server.py
     ```
   - The server should now be running locally. You can access the application by visiting `http://localhost:5000` in your web browser.

## Usage:

- Enter text in the provided input box.
- The application will analyze the emotion depicted in the text and display the result.

## Watson NLU API Integration:

This application integrates with the Watson Natural Language Understanding (NLU) API for analyzing text emotions. The `emotion_detector.py` script sends text data to the API endpoint for analysis and retrieves the emotion predictions.

## Contributing:

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.


