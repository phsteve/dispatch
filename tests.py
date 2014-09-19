import unittest
import json

import maps_api

class MockDistanceFetcher(object):
    def fetch_distance_matrix(self, origins, destination):
        #always returns same data
        f = open('test_data.json')
        json_resp = json.loads(''.join(f.readlines()))
        return json_resp

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.mock_fetcher = MockDistanceFetcher()
        self.mock_analyzer = maps_api.DistanceAnalyzer(self.mock_fetcher)
        self.origins = ['1,1', '2,2']
        self.destination = '3,3'

    def test_get_distances(self):
        distances = self.mock_analyzer.extract_distances(self.origins, self.destination)
        self.assertEquals([48, 181], distances)

    def test_index_of_closest(self):
        self.assertEquals(self.mock_analyzer.index_of_closest([3, 1, 7]), 1)

    def test_find_closest(self):
        closest = self.mock_analyzer.find_closest(self.origins, self.destination)
        self.assertEquals(closest, 0)

    def test_live_find_closest(self):
        fetcher = maps_api.DistanceFetcher()
        analyzer = maps_api.DistanceAnalyzer(fetcher)
        origins = ["456-466 Dekalb Avenue, Brooklyn, NY 11238, USA", "290-292 Gates Avenue, Brooklyn, NY 11216, USA"]
        destination = "256 Ryerson Street, Brooklyn, NY 11205, USA"
        closest = analyzer.find_closest(origins, destination)
        self.assertEquals(closest, 0)

if __name__ == "__main__":
    unittest.main()