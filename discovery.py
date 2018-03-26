import facebook
import json
import sys
import os
import logging

import utils


if __name__ == "__main__":
    logging.basicConfig(filename=utils.get_logfile(), level=utils.log_level)
    utils.log_intro(__file__)

    fb_page_list_file = "fb_page_list.txt"
    event_list_file = "event_list.txt"
    base_req = "{}/events?include_cancelled=false&time_filter=upcoming&fields=id"
    graph = utils.get_facebook_graph()
    venue_list = set(utils.get_disk_list(fb_page_list_file))
    event_list = utils.get_disk_list(event_list_file)
    new_event_ids = set()
    for venue in venue_list:
        fb_venue_req = base_req.format(venue)
        venue_fb_event_ids = graph.get_object(fb_venue_req);
        for event in venue_fb_event_ids["data"]:
            new_event_ids.add(event["id"])

    length_orig = len(event_list)
    event_list.extend(new_event_ids)
    event_list = set(event_list)
    length_no_dupes = len(event_list)
    total_events_added = length_no_dupes - length_orig
    logging.info("Discovery added {} new events to {}".format(total_events_added, event_list_file))
    
    utils.overwrite_disk_list(event_list_file, event_list)
