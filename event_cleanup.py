import os
import json
import sys
import datetime
import dateutil.parser as dp
import logging

import utils

if __name__ == "__main__":
    logging.basicConfig(filename=utils.get_logfile(), level=utils.log_level)
    utils.log_intro(__file__)

    event_loc = utils.jsondump_dir
    current_time = datetime.datetime.now()
    list_of_events = os.listdir(event_loc)
    old_event_ids = set()
    old_event_locs = []
    for event in list_of_events:
        event_path = os.path.join(event_loc, event)
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

    #if old_event_ids has elements
    if old_event_ids:
        logging.info("{} events removed:".format(len(old_event_ids)))
        for event in old_event_ids:
            logging.info(event)
    
