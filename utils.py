import json
import sys
import os
import facebook
import datetime

import logging

template_dir = "templates"
log_dir = "logs"
log_level = logging.INFO
default_event_priority = "9"
jsondump_dir = "jsondump"
pages_filename = "pages.json"

"""
the next 3 methods are duplicates. need to abstract it out
enum?
constants?
"""
def get_header():
    #get document header from template
    doc_head = ""
    file_path = os.path.join(template_dir, "doc_head.html")
    with open(file_path, 'r') as head:
        doc_head = head.read()
    head.close()
    return doc_head

def get_footer():
    #get document footer from template
    doc_foot = ""
    file_path = os.path.join(template_dir, "doc_foot.html")
    with open(file_path, 'r') as foot:
        doc_foot = foot.read()
    foot.close()
    return doc_foot

def get_promo_banner():
    #get document footer from template
    promo = ""
    file_path = os.path.join(template_dir, "promo_banner.html")
    with open(file_path, 'r') as promo_file:
        promo = promo_file.read()
    promo_file.close()
    return promo

def get_pages():
    pages = {}
    with open(pages_filename, 'r') as pages_file:
        pages = json.load(pages_file)
    pages_file.close()
    return pages

def update_pages(new_pages):
    with open(pages_filename, 'w') as pages_file:
        json.dump(new_pages, pages_file)
    pages_file.close()

def get_facebook_graph():
    f = open('access_token.txt', 'r')
    access_token = f.read()
    f.close()
    graph = facebook.GraphAPI(access_token=access_token)
    return graph

def get_logfile():
    date_today = datetime.date.today().isoformat()
    logfile_name = os.path.join(log_dir, date_today) + ".log"
    return logfile_name

def log_intro(parent_script):
    logging.info("{}:{}:".format(datetime.datetime.now().isoformat(),parent_script))
