import facebook
import json
import sys
import os
from sets import Set
import datetime
import dateutil.parser as dp

import utils
#make all strings utf-8 encoding for whole script
reload(sys)
sys.setdefaultencoding('utf-8')

tag_name = "name"
tag_prio = "priority"
tag_id = "id"
tag_desc = "description"

tag_place = "place"
tag_loc = "location"
tag_city = "city"
tag_state = "state"
#note: the venue tag in the data is at place -> name. this is use for ev_data key
tag_venue = "venue"

tag_start_year = "start_year"
tag_start_month = "start_month"
tag_start_month_name = "start_month_name"
tag_start_day = "start_day"
tag_start_weekday = "start_weekday"
#with am/pm
tag_start = "start_time"

tag_end_year = "end_year"
tag_end_month = "end_month"
tag_end_month_name = "end_month_name"
tag_end_day = "end_day"
tag_end_weekday = "end_weekday"
#with am/pm
tag_end = "end_time"

NONE_SPECIFIED = "None Specified"

filters_start_html = """
    <div id="filter-block" class="container">
        <div class="panel">
            <div class="panel-body">
                <div class="row">
"""
filters_end_html = """
                    <div class="pull-right">
                        <div id="filter-btns" class="btn-group">
                            <button type="button" id="filter-reset" class="btn btn-primary" data-toggle="tooltip" title="Reset Events">
                                <span class="glyphicon glyphicon-refresh"></span>
                            </button>
                            <button type="button" id="filter-submit" class="btn btn-primary" data-toggle="tooltip" title="Apply Filters">
                                <span class="glyphicon glyphicon-filter"></span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

def create_content_filter(filter_list, filter_on, default_option):
    start_html = """
                    <div class="col-sm-3 filter-column">
                        <select id="{0}-filter" class="form-control filter-master" data-toggle="tooltip" title="Choose a {2}">
                            <option value="0" selected="selected">{1}</option>""".format(filter_on, default_option,filter_on.capitalize())
    end_html = """
                        </select>
                    </div>
    """
    return_html = start_html
    for filter_item in filter_list:
        return_html += """
                            <option>""" + filter_item + "</option>" 
    return_html += end_html
    return return_html

event_block_beginning = """
    
    <!-- events -->
    <div id="event-block" class="container">
        <div class="row">"""
event_block_end = """
        </div>
    </div>
"""
def create_event_block(ev_data):
    thumbnail_html = """
            <div class="col-sm-6 col-md-4 col-lg-3 event">
                <div class="thumbnail">
                    <div class="caption">
                        <h4 class="event_name" data-toggle="tooltip" title="{name}"> {name} </h3>
                        <hr/>
                        <div class="date">
                            <div class="start_date" data-toggle="tooltip" title="{start_weekday}, {start_month_name} {start_day}, {start_year}">
                                <p>
                                    <span class="glyphicon glyphicon-calendar"></span>
                                    <span class="weekday">{start_weekday}, </span>
                                    <span class="month">{start_month_name} </span>
                                    <span class="day">{start_day}, </span>
                                    <span class="year">{start_year}</span>
                                </p>
                                <p>
                                    <span class="glyphicon glyphicon-time"></span>
                                    <span class="time">{start_time}</span>
                                </p>
                            </div>
                        </div>
                        <p class="venue" data-toggle="tooltip" title="{venue}">
                            <span class="glyphicon glyphicon-flag"></span>
                            {venue}
                        </p>
                        <p class="location"> 
                            <span class="glyphicon glyphicon-globe"></span>
                            <span class="city">{city}</span>, <span class="state">{state}</span>
                        </p>
                        <div hidden class="priority"> {priority} </div>
                        <div hidden class="ev-id"> {ev_id} </div>
                        <button type="button" id="desc-{ev_id}" class="btn desc-btn" onclick="ga('send','event','description', '{ev_id}');" data-toggle="modal" data-target="#modal-{ev_id}" data-toggle="tooltip" title="View Event Description">
                            <span class="glyphicon glyphicon-info-sign"></span>
                            View Details
                        </button>
                        <a href="http://www.facebook.com/events/{ev_id}" class="btn fb-link" role="button" target="_blank" data-toggle="tooltip" title="View Event On Facebook"><i class="fa fa-facebook"></i></a>"""
    modal_html ="""
                        <div class="modal fade" id="modal-{ev_id}" tabindex="-1" role="dialog" aria-labelledby="EventDetails">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                        <h4 class="modal-title"> {name} </h4>
                                        <h6 class="modal-title">
                                            <div class="start_date">
                                                <span class="weekday">{start_weekday}, </span>
                                                <span class="month">{start_month_name} </span>
                                                <span class="day">{start_day}, </span>
                                                <span class="year">{start_year}</span>
                                                <span class="time">{start_time}</span>"""
    if (ev_data[tag_end] != NONE_SPECIFIED):
        modal_html +="""
                                                -
                                                <span class="weekday">{end_weekday}, </span>
                                                <span class="month">{end_month_name} </span>
                                                <span class="day">{end_day}, </span>
                                                <span class="year">{end_year}</span>
                                                <span class="time">{end_time}</span>"""
    modal_html +="""
                                            </div>
                                        </h6>
                                    </div>
                                    <div class="modal-body">
                                        <p> {desc} </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""
    return_html = (thumbnail_html + modal_html).format(name = ev_data[tag_name], start_day = ev_data[tag_start_day], start_month = ev_data[tag_start_month], start_month_name = ev_data[tag_start_month_name], start_year = ev_data[tag_start_year], start_time = ev_data[tag_start], end_day = ev_data[tag_end_day], end_month = ev_data[tag_end_month], end_month_name = ev_data[tag_end_month_name], end_year = ev_data[tag_end_year], end_time = ev_data[tag_end], city = ev_data[tag_city], state = ev_data[tag_state], venue = ev_data[tag_venue], priority = ev_data[tag_prio], ev_id = ev_data[tag_id], desc = ev_data[tag_desc], start_weekday = ev_data[tag_start_weekday], end_weekday = ev_data[tag_end_weekday])

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
            start_dt_raw = ev_json[tag_start]

            ev_name = ev_json[tag_name]
            ev_priority = ev_json[tag_prio]

            end_dt_raw = NONE_SPECIFIED
            if tag_end in ev_json:
                end_dt_raw = ev_json[tag_end]

            start_dt = dp.parse(start_dt_raw)
            ev_start_day = str(start_dt.day)
            ev_start_month = str(start_dt.month)
            ev_start_month_name = start_dt.strftime("%B")
            ev_start_year = str(start_dt.year)
            ev_start_weekday = start_dt.strftime("%A")
            ev_start = start_dt.strftime("%-I:%M%p")

            if (end_dt_raw == NONE_SPECIFIED):
                ev_end_day = NONE_SPECIFIED
                ev_end_month = NONE_SPECIFIED
                ev_end_month_name = NONE_SPECIFIED
                ev_end_year = NONE_SPECIFIED
                ev_end_weekday = NONE_SPECIFIED
                ev_end = NONE_SPECIFIED
            
            else:
                end_dt = dp.parse(end_dt_raw)
                ev_end_day = str(end_dt.day)
                ev_end_month = str(end_dt.month)
                ev_end_month_name = end_dt.strftime("%B")
                ev_end_year = str(end_dt.year)
                ev_end_weekday = end_dt.strftime("%A")
                ev_end = end_dt.strftime("%-I:%M%p")
            
            ev_desc = NONE_SPECIFIED
            if tag_desc in ev_json:
                ev_desc = ev_json[tag_desc]

            ev_city = NONE_SPECIFIED
            ev_state = NONE_SPECIFIED
            ev_venue = NONE_SPECIFIED
            if tag_place in ev_json:
                if tag_loc in ev_json[tag_place]:
                    if tag_city in ev_json[tag_place][tag_loc]:
                        ev_city = ev_json[tag_place][tag_loc][tag_city]
                    if tag_state in ev_json[tag_place][tag_loc]:
                        ev_state = ev_json[tag_place][tag_loc][tag_state]
                    if tag_name in ev_json[tag_place]:
                        #note: venue lives at place -> name
                        ev_venue = ev_json[tag_place][tag_name]

            ev_data = {tag_name : ev_name, tag_start : ev_start, tag_end : ev_end, tag_city : ev_city, tag_state : ev_state, tag_venue : ev_venue, tag_id : ev_id, tag_prio : ev_priority, tag_desc : ev_desc, tag_start_year : ev_start_year, tag_start_month : ev_start_month, tag_start_day : ev_start_day, tag_start_weekday: ev_start_weekday, tag_end_year : ev_end_year, tag_end_month : ev_end_month, tag_end_day : ev_end_day, tag_end_weekday : ev_end_weekday, tag_start_month_name : ev_start_month_name, tag_end_month_name : ev_end_month_name}
            event_dict[ev_id] = ev_data

        event_file.close()
    return event_dict

def get_ordered_event_list(event_dict):
    ordered_list = []
    #this is super complicated
    #the time thing- split the time by T and take the first part, which is YYYY-MM-DD
    #this is so it categorizes by day and not time of day. Priority would only work if the time was exact as well
    #   tuple in        get tuples                     order by    start_year          start_month       start_day         prio       name
    for ev_id in sorted(event_dict.iteritems(), key=lambda (k,v): (v[tag_start_year],v[tag_start_month],v[tag_start_day],v[tag_prio],v[tag_name])):
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
        event_blocks.append(create_event_block(event))

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
        new_index.write(create_content_filter(cities_sorted, tag_city, "All Cities"))
        new_index.write(create_content_filter(states_sorted, tag_state, "All States"))
        new_index.write(create_content_filter(venues_sorted, tag_venue, "All Venues"))
        new_index.write(filters_end_html)
        #start the event block
        new_index.write(event_block_beginning)
        for block in event_blocks:
            new_index.write(block)

        new_index.write(event_block_end)
        new_index.write(doc_foot)
    new_index.close()
