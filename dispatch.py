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


if __name__ == '__main__':
    #print foo(['40.690574,-73.958873', '40.685709,-73.955226'], '40.689947,-73.964302')
    # f = open('test_data.json')
    # json_resp = json.loads(''.join(f.readlines()))
    # distances = get_distances(json_resp)
    # print get_distances(json_resp)
    lst = [3, 1, 7]
    print choose_index(lst)