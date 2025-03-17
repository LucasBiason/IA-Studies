import unittest
from walter.agent import Walter

class TestWalter(unittest.TestCase):
    def setUp(self):
        self.walter = Walter()

    def test_process_youtube_link(self):
        result = self.walter.process_message("https://www.youtube.com/watch?v=fCbdpokrb4E")
        self.assertIn("output", result)

    def test_process_video_link(self):
        video_link = 'tests/testfiles/test_video.mp4'
        result = self.walter.process_message(video_link)
        self.assertIn("output", result)

    def test_process_audio_link(self):
        audio_link = 'tests/testfiles/test_audio.mp3'
        result = self.walter.process_message(audio_link)
        self.assertIn("output", result)

    def test_process_image_link(self):
        image_link = 'tests/testfiles/test_image.png'
        result = self.walter.process_message(image_link)
        self.assertIn("output", result)

if __name__ == '__main__':
    unittest.main()