import json
import sys
import os


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

