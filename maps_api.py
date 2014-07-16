import requests
import json

base_url = 'http://maps.googleapis.com/maps/api/distancematrix/json'

def fetch_distance_matrix(ambulances, job):
    #ambulance = string of "lat,lon"
    #job = string of "lat,lon"
    payload = {'origins': '|'.join(ambulances), 'destinations': job}
    resp = requests.get(base_url, params=payload)
    json_resp = json.loads(resp.content)
    return json_resp

def get_distances(distance_matrix):
    return [row['elements'][0]['duration']['value'] for row in distance_matrix['rows']]

def choose_index(distances):
    smallest = min(distances)
    return distances.index(smallest)
