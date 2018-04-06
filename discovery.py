import facebook
import json
import requests
import sys
import os
import logging

import utils

priority = "priority"
page_owners ="owners"

if __name__ == "__main__":
    logging.basicConfig(filename=utils.get_logfile(), level=utils.log_level)
    utils.log_intro(__file__)

    base_req = "{}/events?fields=place,description,end_time,event_times,id,interested_count,maybe_count,start_time,attending_count,name&time_filter=upcoming&include_cancelled=false"
    graph = utils.get_facebook_graph()
    pages = utils.get_pages()

    all_events = {}

    for page in pages:
        page_priority = pages[page]
        discovery_req = base_req.format(page)
        event_list = graph.get_object(discovery_req);
        while True:
            for event in event_list["data"]:
                ev_id = event['id']
                owners_list = [page]
                new_priority = page_priority
                if ev_id in all_events:
                    logging.debug("Event id {} has multiple owners. Combining information".format(ev_id))
                    duplicate_event = all_events[ev_id]
                    owners_list.extend(duplicate_event[page_owners])
                    if duplicate_event[priority] < new_priority:
                        new_priority = duplicate_event[priority]
 
                event.update({priority: new_priority, page_owners: owners_list})
                all_events[ev_id] = event

            try:
                if "next" in event_list["paging"]:
                    next_request = event_list['paging']['next']
                    logging.debug("Traversing next page for page: {}".format(page))
                    logging.debug("Next page: {}".format(next_request))
                    event_list = requests.get(next_request).json()
                else:
                    break

            except KeyError:
                break

    for event in all_events:
        event_filename = os.path.join(utils.jsondump_dir, event) + ".json"
        with open(event_filename, 'w') as event_json:
            json.dump(all_events[event],event_json)
        event_json.close()

    logging.info("Discovery ended. Number of Events: {}".format(len(all_events)))
