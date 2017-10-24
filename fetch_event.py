import facebook
import json
import sys
import os

def get_facebook_graph():
    f = open('access_token.txt', 'r')
    access_token = f.read()
    f.close()
    graph = facebook.GraphAPI(access_token=access_token)
    return graph

def get_event_info(graph, event_id):
    return graph.get_object(event_id) 

if __name__ == "__main__":
    graph = get_facebook_graph()
    print("Got graph")
    event_id = sys.argv[1]
    fb_event = get_event_info(graph, event_id)
    print(fb_event)
    new_file_name = '../facebookeventjsondump/events/' + event_id + '.json'
    with open(new_file_name, 'w') as event_json_file:
        json.dump(fb_event, event_json_file)

    event_json_file.close()
