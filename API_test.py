# coding = utf-8

from API_utils import *
import unittest2


class Movie(unittest2.TestCase):
    def setUp(self):
        self.host = u"https://movie.douban.com"
        self.api_test_1_uri = u"/subject/1304102/"
        self.api_test_2_uri = u"/subject/1292052/"

    def test_Matt_in_ActorList(self):
        # Test Matt Damon is not in actors list of the movie, which subject id is 1304102.
        res = get(uri=self.api_test_1_uri, host=self.host)
        self.assertNotIn("celebrity/1054443", res.content)

    def test_Top_250(self):
        # Test whether movie, which subject id is 1292052, is the first one in the Top 250 movies.
        res = get(uri=self.api_test_2_uri, host=self.host)
        self.assertIn('<span class="top250-no">No.1</span>', res.content)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest2.main()
