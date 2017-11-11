import json
import sys
import os
import facebook


template_dir = "templates/"

def get_header():
    #get document header from template
    doc_head = ""
    file_path = os.path.join(template_dir, "doc_head.txt")
    with open(file_path, 'r') as head:
        doc_head = head.read()
    head.close()
    return doc_head

def get_footer():
    #get document footer from template
    doc_foot = ""
    file_path = os.path.join(template_dir, "doc_foot.txt")
    with open(file_path, 'r') as foot:
        doc_foot = foot.read()
    foot.close()
    return doc_foot

def get_event_list(event_list_disk):
    event_list = {}
    with open(event_list_disk, 'r') as event_list_file:
        event_list = event_list_file.read().splitlines()
    event_list_file.close()
    return event_list

def get_facebook_graph():
    f = open('access_token.txt', 'r')
    access_token = f.read()
    f.close()
    graph = facebook.GraphAPI(access_token=access_token)
    return graph

