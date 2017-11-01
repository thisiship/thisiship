import facebook
import json
import sys
import os
from sets import Set

import utils

def get_event_link_html(event_id):
    event_link = "    <p><a href=\"view_event.html?event_id=" + event_id + "\"> "
    event_link += event_id + " </a></p>\n"
    return event_link

def create_city_filter(cities_list):
    start_html = """
    <div class="container">
	<div class="panel">
            <div class="panel-body">
                <div class="row">
                    <div class="col-xs-8 col-xs-offset-2 col-sm-6 col-sm-offset-3 col-md-4 col-md-offset-4">
                        <select class="form-control city-filter">
                            <option selected="selected">All Cities</option>"""
    end_html = """
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return_html = start_html
    for city in cities_list:
        return_html += """
                            <option>""" + city + "</option>" 
    return_html += end_html
    return return_html
event_block_beginning = """
    
    <!-- events -->
    <div class="container">
        <div class="row event-list">"""
event_block_end = """
        </div>
    </div>
"""
def create_event_block(ev_name, ev_start, ev_end, ev_city, ev_state, ev_venue, ev_id, ev_priority):
   return_html = """
            <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 event">
                <div class="thumbnail">
                    <div class="caption">
                        <h4 class="event_name">%s</h3>
                        <p class="date">
                            <span class="start_date">%s</span> - <span class="end_date">%s</span>
                        </p>
                        <p class="location"> 
                            <span class="city">%s</span>, <span class="state">%s</span>
                        </p>
                        <p class="venue"> %s </p>
                        <p><a href="view_event.html?event_id=%s" class="btn btn-primary" role="button"> Details </a></p>
                        <div hidden class="priority"> %s </div>
                    </div>
                </div>
            </div>
   """ % (ev_name,ev_start,ev_end,ev_city,ev_state,ev_venue,ev_id,ev_priority)

   return return_html

if __name__ == "__main__":
    doc_head = utils.get_header()
    doc_foot = utils.get_footer()
    event_loc = "jsondump/"
    list_of_events = os.listdir(event_loc)
    events_html = ""
    cities_list = Set([])
    states_list = Set([])
    venue_list = Set([])
    event_blocks = []
    for event in list_of_events:
        #the only things an event is required to have are:
        #   id 
        #   start_time
        #   name
        with open(event_loc + event) as event_file:
            ev_json = json.load(event_file)

            ev_id = ev_json["id"]
            ev_start = ev_json["start_time"]
            ev_name = ev_json["name"]
            ev_priority = ev_json["priority"]

            ev_end = "None Specified"
            if "end_time" in ev_json:
                ev_end = ev_json["end_time"]

            ev_city = "None Specified"
            ev_state = "None Specified"
            ev_venue = "None Specified"
            if "place" in ev_json:
                if "location" in ev_json["place"]:
                    if "city" in ev_json["place"]["location"]:
                        ev_city = ev_json["place"]["location"]["city"]
                        cities_list.add(ev_city)
                    if "state" in ev_json["place"]["location"]:
                        ev_state = ev_json["place"]["location"]["state"]
                        states_list.add(ev_state)
                    if "name" in ev_json["place"]:
                        ev_venue = ev_json["place"]["name"]
                        venue_list.add(ev_venue)
            event_blocks.append(create_event_block(ev_name, ev_start, ev_end, ev_city, ev_state, ev_venue, ev_id, ev_priority))

        event_file.close()


    with open ("index.html",'w') as new_index:
        new_index.write(doc_head)
        #turn sets into alphabetical lists
        cities_sorted = sorted(cities_list)
        states_sorted = sorted(states_list)
        venues_sorted = sorted(venue_list)
        #write the filter bar
        new_index.write(create_city_filter(cities_sorted))
        #start the event block
        new_index.write(event_block_beginning)
        for event in event_blocks:
            new_index.write(event)
        new_index.write(event_block_end)
        new_index.write(doc_foot)
    new_index.close()
