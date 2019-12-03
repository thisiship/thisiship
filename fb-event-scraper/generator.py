# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape
import json
import os

env = Environment(loader=PackageLoader(__name__, 'templates'), autoescape=select_autoescape(['html', 'xml']), trim_blocks=True, lstrip_blocks=True)

def get_event_data():
    events_dir = "./events"
    event_dict = []
    event_filenames = sorted([x for x in os.listdir(events_dir) if x.endswith('.json')])

    for filename in event_filenames:
        with open(os.path.join(events_dir, filename)) as f:
            event_dict.append(json.load(f))
        f.close()
    return event_dict


def generate_index(event_data):
    template = env.get_template("index.html")

    index_template = template.render(event_list=event_data)
    with open("index.html", 'w') as new_index:
        new_index.write(index_template)
    new_index.close()

if __name__ == "__main__":
    # song_dict = generate_songs()
    # generate_index(song_dict)
    event_data = get_event_data()
    generate_index(event_data)
