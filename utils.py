import json
import sys
import os
import facebook


template_dir = "templates/"

"""
the next 3 are duplicates. need to abstract it out
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


#this is used to get the data from event,venue,band lists
def get_disk_list(list_disk_path):
    disk_list = {}
    with open(list_disk_path, 'r') as list_file:
        disk_list = list_file.read().splitlines()
    list_file.close()
    return disk_list

def get_facebook_graph():
    f = open('access_token.txt', 'r')
    access_token = f.read()
    f.close()
    graph = facebook.GraphAPI(access_token=access_token)
    return graph

