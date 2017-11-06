import facebook
import json
import sys
import os
from sets import Set

import utils

tag_name = "name"
tag_start = "start_time"
tag_end = "end_time"
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

filters_start_html = """
    <div class="container">
        <div class="panel">
            <div class="panel-body">
                <div class="row">
"""
filters_end_html = """
                    <div class="col-xs-3">
                        <button type="button" id="filter-submit" class="btn btn-primary">Filter</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""
def create_city_filter(cities_list):
    start_html = """
                    <div class="col-xs-3">
                        <select class="form-control city-filter">
                            <option selected="selected">All Cities</option>"""
    end_html = """
                        </select>
                    </div>
    """
    return_html = start_html
    for city in cities_list:
        return_html += """
                            <option>""" + city + "</option>" 
    return_html += end_html
    return return_html

def create_state_filter(states_list):
    start_html = """
                    <div class="col-xs-3">
                        <select class="form-control state-filter">
                            <option selected="selected">All States</option>"""
    end_html = """
                        </select>
                    </div>
    """
    return_html = start_html
    for state in states_list:
        return_html += """
                            <option>""" + state + "</option>" 
    return_html += end_html
    return return_html

def create_venue_filter(venues_list):
    start_html = """
                    <div class="col-xs-3">
                        <select class="form-control venue-filter">
                            <option selected="selected">All Venues</option>"""
    end_html = """
                        </select>
                    </div>
    """
    return_html = start_html
    for venue in venues_list:
        return_html += """
                            <option>""" + venue + "</option>" 
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
                            <span class="city">%s</span>, <span class="state">%s</span>
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
def create_event_dict(events_loc):
    event_dict = {}
    list_of_events = os.listdir(events_loc)
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
                    if tag_state in ev_json[tag_place][tag_loc]:
                        ev_state = ev_json[tag_place][tag_loc][tag_state]
                    if tag_name in ev_json[tag_place]:
                        #note: venue lives at place -> name
                        ev_venue = ev_json[tag_place][tag_name]
            ev_data = {tag_name : ev_name, tag_start : ev_start, tag_end : ev_end, tag_city : ev_city, tag_state : ev_state, tag_venue : ev_venue, tag_id : ev_id, tag_prio : ev_priority, tag_desc : ev_desc}
            event_dict[ev_id] = ev_data

        event_file.close()
    return event_dict

def get_ordered_event_list(event_dict):
    ordered_list = []
    #this is super complicated
    #the time thing- split the time by T and take the first part, which is YYYY-MM-DD
    #this is so it categorizes by day and not time of day. Priority would only work if the time was exact as well
    #   tuple in        get tuples                     order by    start_time then prio then name
    for ev_id in sorted(event_dict.iteritems(), key=lambda (k,v): (v[tag_start].split('T')[0],v[tag_prio],v[tag_name])):
        #ev_id is the tuple (ev_id, actual event dict)
        ordered_list.append(ev_id[1])
    return ordered_list

if __name__ == "__main__":
    doc_head = utils.get_header()
    doc_foot = utils.get_footer()
    event_loc = "jsondump/"
    index_loc = "index.html"
    event_dict = create_event_dict(event_loc)
    events_ordered = get_ordered_event_list(event_dict)
    event_blocks = []
    for event in events_ordered:
        event_blocks.append(create_event_block(event).encode('utf-8'))

    cities = set()
    states = set()
    venues = set()
    #get all cities, states, venues for filtering purposes
    for event in event_dict:
        cities.add(event_dict[event][tag_city])
        states.add(event_dict[event][tag_state])
        venues.add(event_dict[event][tag_venue])
        
    cities_sorted = sorted(cities)
    states_sorted = sorted(states)
    venues_sorted = sorted(venues)
    with open (index_loc, 'w') as new_index:
        new_index.write(doc_head)
        #write the filter bar
        new_index.write(filters_start_html)
        new_index.write(create_city_filter(cities_sorted))
        new_index.write(create_state_filter(states_sorted))
        new_index.write(create_venue_filter(venues_sorted))
        new_index.write(filters_end_html)
        #start the event block
        new_index.write(event_block_beginning)
        for block in event_blocks:
            new_index.write(block)
        new_index.write(event_block_end)
        new_index.write(doc_foot)
    new_index.close()
