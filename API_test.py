# coding = utf-8

from API_utils import *
import unittest2


class Movie(unittest2.TestCase):
    def setUp(self):
        self.host = u'https://movie.douban.com'
        self.api_test_1_uri = u"/subject/1304102/"
        self.api_test_2_uri = u"/subject/1292052/"

    def test_Matt_in_ActorList(self):
        res = get(uri=self.api_test_1_uri)
        self.assertIn("celebrity/1054443", res.content)

    def test_Top_250(self):
        res = get(uri=self.api_test_2_uri)
        self.assertIn("top250", res.content)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest2.main()
