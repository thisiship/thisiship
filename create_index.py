import facebook
import json
import sys
import os
from sets import Set
import datetime
import dateutil.parser as dp
import logging

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
tag_locale = "locale"
tag_city = "city"
tag_state = "state"
#note: the venue tag in the data is at place -> name. this is use for ev_data key
tag_venue = "venue"

tag_start_year = "start_year"
tag_start_month = "start_month"
tag_start_month_name = "start_month_name"
tag_start_day = "start_day"
tag_start_weekday = "start_weekday"
tag_start_datetime = "start_datetime"
#with am/pm
tag_start = "start_time"

tag_end_year = "end_year"
tag_end_month = "end_month"
tag_end_month_name = "end_month_name"
tag_end_day = "end_day"
tag_end_weekday = "end_weekday"
tag_end_datetime = "end_datetime"
#with am/pm
tag_end = "end_time"

tag_event_times = "event_times"

NONE_SPECIFIED = "None Specified"

filters_start_html = """
    <div id="filter-block" class="container">
        <div class="panel">
            <div class="panel-body">
                <div class="row">
                    <div class="col-sm-4 filter-column">
                        <input type="date" id="filter-date" class="filter-master form-control" data-target="{}" title="Choose a Start Date">
                    </div>
""".format(tag_start_datetime)

filters_end_html = """
                    <div class="pull-right">
                        <div id="filter-btns" class="btn-group">
                            <button type="button" id="filter-reset" class="btn btn-primary" data-toggle="tooltip" title="Reset Events">
                                <span class="glyphicon glyphicon-refresh"></span>
                                Reset
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
                    <div class="col-sm-4 filter-column">
                        <select id="filter-{0}" class="form-control filter-master" data-toggle="tooltip" data-target={0} title="Choose a {2}">
                            <option value="0" selected="selected">{1}</option>""".format(filter_on, default_option,filter_on.capitalize())
    end_html = """
                        </select>
                    </div>
    """
    return_html = start_html
    for filter_item in filter_list:
        return_html += """
                            <option value="{1}">{0}</option>""".format(filter_item, filter_item.lower())
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
                        <div hidden class="priority" value="{priority}"></div>
                        <div hidden class="ev-id" value="{ev_id}"></div>
                        <div hidden class="start_datetime" value="{start_datetime}"></div>
                        <div hidden class="end_datetime" value="{end_datetime}"></div>
                        <div hidden class="locale" value="{locale}"></div>
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
                        <p class="venue" data-toggle="tooltip" title="{venue}" value="{venue}">
                            <span class="glyphicon glyphicon-flag"></span>
                            {venue}
                        </p>
                        <p class="location"> 
                            <span class="glyphicon glyphicon-globe"></span>
                            <span class="city" value="{city}">{city}</span>, <span class="state" value="{state}">{state}</span>
                        </p>
                        <button type="button" id="desc-{ev_id}" class="btn desc-btn" data-toggle="modal" data-target="#modal-{ev_id}" data-toggle="tooltip" title="View Event Description">
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
    return_html = (thumbnail_html + modal_html).format(name = ev_data[tag_name], start_day = ev_data[tag_start_day], start_month = ev_data[tag_start_month], start_month_name = ev_data[tag_start_month_name], start_year = ev_data[tag_start_year], start_time = ev_data[tag_start], end_day = ev_data[tag_end_day], end_month = ev_data[tag_end_month], end_month_name = ev_data[tag_end_month_name], end_year = ev_data[tag_end_year], end_time = ev_data[tag_end], city = ev_data[tag_city], state = ev_data[tag_state], venue = ev_data[tag_venue], priority = ev_data[tag_prio], ev_id = ev_data[tag_id], desc = ev_data[tag_desc], start_weekday = ev_data[tag_start_weekday], end_weekday = ev_data[tag_end_weekday], start_datetime = ev_data[tag_start_datetime], end_datetime = ev_data[tag_end_datetime], locale = ev_data[tag_locale])

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

            ev_name = ev_json[tag_name]
            ev_priority = ev_json[tag_prio]

            start_dt_raw = ev_json[tag_start]
            end_dt_raw = NONE_SPECIFIED

            if tag_event_times in ev_json:
                event_times = ev_json[tag_event_times]
                #this list comes in in reverse chronological. Reverse it.
                event_times.reverse()
                if event_times is None or len(event_times) == 0:
                    logging.info("Recurring event found with empty {} tag. Omitting event id {}".format(tag_event_times, ev_id))
                    continue

                current_time = datetime.datetime.now().isoformat()
                for ev_time in event_times:
                    ev_start = ev_time[tag_start]
                    #pick the first event time you find that starts after now
                    if ev_start > current_time:
                        start_dt_raw = ev_start
                        if tag_end in ev_time:
                            end_dt_raw = ev_time[tag_end]

                        logging.debug("Recurring event {} found. Start: {} | End: {} ".format(ev_id,start_dt_raw,end_dt_raw))
                        #we found the earliest event that happens after today, skip the rest of the event_times
                        break


            if end_dt_raw == NONE_SPECIFIED and tag_end in ev_json:
                end_dt_raw = ev_json[tag_end]

            start_dt = dp.parse(start_dt_raw)
            ev_start_day = str(start_dt.day)
            ev_start_month = str(start_dt.month)
            ev_start_month_name = start_dt.strftime("%B")
            ev_start_year = str(start_dt.year)
            ev_start_weekday = start_dt.strftime("%A")
            ev_start = start_dt.strftime("%-I:%M%p")
            ev_start_datetime = start_dt.date().isoformat()

            if (end_dt_raw == NONE_SPECIFIED):
                ev_end_day = NONE_SPECIFIED
                ev_end_month = NONE_SPECIFIED
                ev_end_month_name = NONE_SPECIFIED
                ev_end_year = NONE_SPECIFIED
                ev_end_weekday = NONE_SPECIFIED
                ev_end = NONE_SPECIFIED
                ev_end_datetime = NONE_SPECIFIED
            
            else:
                end_dt = dp.parse(end_dt_raw)
                ev_end_day = str(end_dt.day)
                ev_end_month = str(end_dt.month)
                ev_end_month_name = end_dt.strftime("%B")
                ev_end_year = str(end_dt.year)
                ev_end_weekday = end_dt.strftime("%A")
                ev_end = end_dt.strftime("%-I:%M%p")
                ev_end_datetime = end_dt.date().isoformat()
            
            ev_desc = NONE_SPECIFIED
            if tag_desc in ev_json:
                ev_desc = ev_json[tag_desc]

            ev_city = NONE_SPECIFIED
            ev_state = NONE_SPECIFIED
            ev_venue = NONE_SPECIFIED
            ev_locale = NONE_SPECIFIED
            if tag_place in ev_json:
                if tag_loc in ev_json[tag_place]:
                    if tag_city in ev_json[tag_place][tag_loc]:
                        ev_city = ev_json[tag_place][tag_loc][tag_city]
                    if tag_state in ev_json[tag_place][tag_loc]:
                        ev_state = ev_json[tag_place][tag_loc][tag_state]
                    if tag_name in ev_json[tag_place]:
                        #note: venue lives at place -> name
                        ev_venue = ev_json[tag_place][tag_name]

                    ev_locale = "{}, {}".format(ev_city, ev_state)

            ev_data = {tag_name : ev_name, tag_start : ev_start, tag_end : ev_end, tag_city : ev_city, tag_state : ev_state, tag_venue : ev_venue, tag_id : ev_id, tag_prio : ev_priority, tag_desc : ev_desc, tag_start_year : ev_start_year, tag_start_month : ev_start_month, tag_start_day : ev_start_day, tag_start_weekday: ev_start_weekday, tag_end_year : ev_end_year, tag_end_month : ev_end_month, tag_end_day : ev_end_day, tag_end_weekday : ev_end_weekday, tag_start_month_name : ev_start_month_name, tag_end_month_name : ev_end_month_name, tag_start_datetime : ev_start_datetime, tag_end_datetime : ev_end_datetime, tag_locale : ev_locale}
            event_dict[ev_id] = ev_data

        event_file.close()
    return event_dict

def get_ordered_event_list(event_dict):
    ordered_list = []
    #this is super complicated
    #the time thing- split the time by T and take the first part, which is YYYY-MM-DD
    #this is so it categorizes by day and not time of day. Priority would only work if the time was exact as well
    #   tuple in        get tuples                     order by    start_year          start_month       start_day         prio       name
    for ev_id in sorted(event_dict.iteritems(), key=lambda (k,v): (int(v[tag_start_year]),int(v[tag_start_month]),int(v[tag_start_day]),int(v[tag_prio]),v[tag_name])):
        #ev_id is the tuple (ev_id, actual event dict)
        ordered_list.append(ev_id[1])
    return ordered_list

if __name__ == "__main__":
    logging.basicConfig(filename=utils.get_logfile(), level=utils.log_level)
    utils.log_intro(__file__) 

    doc_head = utils.get_header()
    doc_foot = utils.get_footer()
    promo_banner = utils.get_promo_banner()
    event_loc = "jsondump/"
    index_loc = "index.html"
    event_dict = create_event_dict(event_loc)
    events_ordered = get_ordered_event_list(event_dict)
    event_blocks = []
    for event in events_ordered:
        event_blocks.append(create_event_block(event))

    locations = set()
    venues = set()
    #get all cities, states, venues for filtering purposes
    for event in event_dict:
        loc = "{}, {}".format(event_dict[event][tag_city], event_dict[event][tag_state])
        locations.add(loc)
        venues.add(event_dict[event][tag_venue])
        
    venues_sorted = sorted(venues)
    locations_sorted = sorted(locations)
    with open (index_loc, 'w') as new_index:
        new_index.write(doc_head)
        new_index.write(promo_banner)
        #write the filter bar
        new_index.write(filters_start_html)
        new_index.write(create_content_filter(locations_sorted, tag_locale, "All Locations"))
        new_index.write(create_content_filter(venues_sorted, tag_venue, "All Venues"))
        new_index.write(filters_end_html)
        #start the event block
        new_index.write(event_block_beginning)
        for block in event_blocks:
            new_index.write(block)

        new_index.write(event_block_end)
        new_index.write(doc_foot)
    new_index.close()
