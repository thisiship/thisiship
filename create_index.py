import facebook
import json
import sys
import os
from sets import Set

import utils

tag_name = "name"
tag_start = "start_time"
tag_end = "end-time"
tag_prio = "priority"
tag_id = "id"
tag_desc = "description"
tag_place = "place"
tag_loc = "location"
tag_city = "city"
tag_state = "state"
#note: the venue tag in the data is at place -> name. this is use for ev_data key
tag_venue = "venue"
none_specified = "None Specified"

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
def create_event_block(ev_data):
   return_html = """
            <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 event">
                <div class="thumbnail">
                    <div class="caption">
                        <h4 class="event_name"> %s </h3>
                        <p class="date">
                            <span class="start_date"> %s </span> - <span class="end_date"> %s </span>
                        </p>
                        <p class="location"> 
                            <span class="city"> %s </span>, <span class="state"> %s </span>
                        </p>
                        <p class="venue"> %s </p>
                        <div hidden class="priority"> %s </div>
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#modal-%s">View Details</button>
                        <a href="http://www.facebook.com/events/%s" class="btn btn-primary" role="button" target="_blank">Facebook Event</a>
                        <div class="modal fade" id="modal-%s" tabindex="-1" role="dialog" aria-labelledby="EventDetails">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                        <h4 class="modal-title"> %s </h4>
                                    </div>
                                    <div class="modal-body">
                                        <p> %s </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
   """ % (ev_data[tag_name],ev_data[tag_start],ev_data[tag_end],ev_data[tag_city],ev_data[tag_state],ev_data[tag_venue],ev_data[tag_prio],ev_data[tag_id],ev_data[tag_id],ev_data[tag_id],ev_data[tag_name],ev_data[tag_desc])

   return return_html


if __name__ == "__main__":
    doc_head = utils.get_header()
    doc_foot = utils.get_footer()
    event_loc = "jsondump/"
    index_loc = "index.html"
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

            ev_id = ev_json[tag_id]
            ev_start = ev_json[tag_start]
            ev_name = ev_json[tag_name]
            ev_priority = ev_json[tag_prio]

            ev_end = none_specified
            if tag_end in ev_json:
                ev_end = ev_json[tag_end]
            
            ev_desc = none_specified
            if tag_desc in ev_json:
                ev_desc = ev_json[tag_desc]

            ev_city = none_specified
            ev_state = none_specified
            ev_venue = none_specified
            if tag_place in ev_json:
                if tag_loc in ev_json[tag_place]:
                    if tag_city in ev_json[tag_place][tag_loc]:
                        ev_city = ev_json[tag_place][tag_loc][tag_city]
                        cities_list.add(ev_city)
                    if tag_state in ev_json[tag_place][tag_loc]:
                        ev_state = ev_json[tag_place][tag_loc][tag_state]
                        states_list.add(ev_state)
                    if tag_name in ev_json[tag_place]:
                        #note: venue lives at place -> name
                        ev_venue = ev_json[tag_place][tag_name]
                        venue_list.add(ev_venue)
            ev_data = {tag_name : ev_name, tag_start : ev_start, tag_end : ev_end, tag_city : ev_city, tag_state : ev_state, tag_venue : ev_venue, tag_id : ev_id, tag_prio : ev_priority, tag_desc : ev_desc}
            event_blocks.append(create_event_block(ev_data))

        event_file.close()


    with open (index_loc, 'w') as new_index:
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
            new_index.write(event.encode('utf-8'))
        new_index.write(event_block_end)
        new_index.write(doc_foot)
    new_index.close()
