import facebook
import json
import sys
import os
import logging

import utils

def get_event_info(graph, event_id):
    return graph.get_object(event_id) 

if __name__ == "__main__":
    logging.basicConfig(filename=utils.get_logfile(), level=utils.log_level)
    utils.log_intro(__file__)

    event_list_disk = "event_list.txt"
    jsondump_loc = "jsondump"
    graph = utils.get_facebook_graph()
    event_list = set(utils.get_disk_list(event_list_disk))
    valid_event = False
    invalid_event_ids_to_delete = []
    for event_id in event_list:
        if (event_id is not None and event_id != ""):
            new_file_name = os.path.join(jsondump_loc, event_id) + '.json'
 
            fb_event = {}
            try:
                fb_event = get_event_info(graph, event_id)
                valid_event = True
            except facebook.GraphAPIError:
                valid_event = False
                invalid_event_ids_to_delete.append(event_id)
                continue

            event_priority = utils.default_event_priority

            if (os.path.exists(new_file_name)):
                #the file does exist. get priority from it
                with open(new_file_name, 'r') as existing_file:
                    event_json = json.load(existing_file)
                    event_priority = event_json["priority"]
                existing_file.close()
            else:
                #the file doesn't exist. add new file with default prio
                logging.info("New Event: %s" % new_file_name)

            fb_event["priority"] = event_priority
            with open(new_file_name, 'w') as event_json_file:
                json.dump(fb_event, event_json_file)

            event_json_file.close()

    if len(invalid_event_ids_to_delete) > 0:
        invalid_event_ids_to_delete = set(invalid_event_ids_to_delete)
        new_event_list = event_list - invalid_event_ids_to_delete
        utils.overwrite_disk_list(event_list_disk,new_event_list)
        for event_id in invalid_event_ids_to_delete:
            json_file_loc = os.path.join(jsondump_loc, event_id) + '.json'
            if os.path.exists(json_file_loc):
                os.remove(json_file_loc)
            logging.info("{} is an invalid event. Removed it from {}".format(event_id,event_list_disk))
