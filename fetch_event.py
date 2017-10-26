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

def get_event_list(event_list_disk):
    event_list = {}
    with open(event_list_disk, 'r') as event_list_file:
        event_list = event_list_file.read().splitlines()
    event_list_file.close()
    return event_list

if __name__ == "__main__":
    event_list_disk = "event_list.txt"
    jsondump_loc = "jsondump/"
    graph = get_facebook_graph()
    print("Got graph")
    event_list = get_event_list(event_list_disk); 
    for event_id in event_list:
        if (event_id is not None and event_id != ""):
            print(event_id)
            fb_event = get_event_info(graph, event_id)
            new_file_name = jsondump_loc  + event_id + '.json'
            #events have default priority 0
            event_priority = "0"

            if (os.path.exists(new_file_name)):
                print("Event exists already. Saving priority.")
                #the file does exist. get priority from it
                with open(new_file_name, 'r') as existing_file:
                    event_json = json.load(existing_file)
                    event_priority = event_json["priority"]
                existing_file.close()
            else:
                #the file doesn't exist. add new file with default prio
                print("Failed to find existing event: " + event_id)

            fb_event["priority"] = event_priority
            with open(new_file_name, 'w') as event_json_file:
                json.dump(fb_event, event_json_file)

            event_json_file.close()
