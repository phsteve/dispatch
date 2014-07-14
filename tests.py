import unittest
import json
import dispatch

class TestMapsApi(unittest.TestCase):
    def test_get_distances(self):
        f = open('test_data.json')
        json_resp = json.loads(''.join(f.readlines()))
        distances = dispatch.get_distances(json_resp)
        self.assertEquals(distances, [48, 181])

    def test_choose_index(self):
        pass

if __name__ == "__main__":
    unittest.main()
