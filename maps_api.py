import requests
import json

class DistanceFetcher(object):
    def __init__(self):
        self.base_url = 'http://maps.googleapis.com/maps/api/distancematrix/json'

    def fetch_distance_matrix(self, origins, destination):
        #origin = string of "lat,lon"
        #destination = string of "lat,lon"
        payload = {'origins': '|'.join(origins), 'destinations': destination}
        resp = requests.get(self.base_url, params=payload)
        json_resp = json.loads(resp.content)
        return json_resp

class DistanceAnalyzer(object):
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def extract_distances(self, origins, destination):
        distance_matrix = self.fetcher.fetch_distance_matrix(origins, destination)
        #distance_matrix is json in the format specified at
        #https://developers.google.com/maps/documentation/distancematrix/#JSON
        return [row['elements'][0]['duration']['value'] for row in distance_matrix['rows']]

    @staticmethod
    def index_of_closest(distances):
        #distances = list of distances (ints)
        #we just return the index of the first, smallest distance.
        #may eventually want indices of smallest three, say
        return distances.index(min(distances))

    def find_closest(self, origins, destination):
        return self.index_of_closest(self.extract_distances(origins, destination))
