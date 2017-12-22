import os
import json
import sys
import datetime
import dateutil.parser as dp
import utils

if __name__ == "__main__":
    event_loc = "jsondump/"
    event_list_loc = "event_list.txt"
    current_time = datetime.datetime.now()
    list_of_events = os.listdir(event_loc)
    old_event_ids = set()
    old_event_locs = []
    for event in list_of_events:
        event_path = event_loc + event
        with open(event_path) as event_file:
            ev_json = json.load(event_file)
            ev_id = ev_json["id"]
            if "end_time" in ev_json:
                ev_time = ev_json["end_time"]
            else:
                ev_time = ev_json["start_time"]
            result = dp.parse(ev_time)
            if (result.replace(tzinfo=None) < current_time):
                old_event_locs.append(event_path)
                old_event_ids.add(ev_id)

        event_file.close()
 
    for event in old_event_locs:
        os.remove(event)

    ev_list = set(utils.get_disk_list(event_list_loc))
    new_ev_list = ev_list - old_event_ids
    with open(event_list_loc, 'w') as new_event_list:
        for event in new_ev_list:
            new_event_list.write(event + "\n")
    new_event_list.close()
    #if old_event_ids has elements
    if old_event_ids:
        print("{} events removed.".format(len(old_event_ids)))
        print("Events removed:")
        for event in old_event_ids:
            print(event)
    
