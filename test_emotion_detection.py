import unittest
from emotion_detector import emotion_detector

class TestEmotion(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")

if __name__ == "__main__":
    unittest.main() 