import unittest
from src.playback_buffer import PlaybackBuffer

class TestPlaybackBuffer(unittest.TestCase):
    def test_exists(self):
        buffer = PlaybackBuffer()
        self.assertIsNotNone(buffer)

if __name__ == '__main__':
    unittest.main()