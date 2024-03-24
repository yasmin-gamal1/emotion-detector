import unittest
from EmotionDetection. emotion_detection import emotion_detector

class EmotionDetectionTestCase(unittest.TestCase):
    def test_joy(self):
        self.assertEqual(self.get_dominant_emotion('I am glad this happened'), 'joy')

    def test_anger(self):
        self.assertEqual(self.get_dominant_emotion('I am really mad about this'), 'anger')

    def test_disgust (self):
        self.assertEqual(self.get_dominant_emotion('I feel disgusted just hearing about this'), 'disgust')

    def test_sadness (self):
        self.assertEqual(self.get_dominant_emotion('I am so sad about this'), 'sadness')

    def test_fear(self):
        self.assertEqual(self.get_dominant_emotion('I am really afraid that this will happen'), 'fear')

    def get_dominant_emotion(self, text_to_analyze):
        emotions = emotion_detector(text_to_analyze)
        return emotions ['dominant_emotion']


if __name__ == '__main__':
    unittest.main()
