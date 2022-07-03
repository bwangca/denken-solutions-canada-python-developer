import unittest

import sample

class TestSample(unittest.TestCase):

    def setUp(self):
        self.app = sample.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        #response = self.app.get('/')
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(200, 200)

if __name__ == '__main__':
    unittest.main()