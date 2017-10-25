import facebook
import json
import sys
import os

head_of_doc = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Website for viewing local music events">
    <meta name="author" content="source - http://github.com/tonisbones">
    <title> This Is Hip </title>

    <script src="js/vendor/jquery.min.js"></script>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <link href="css/thisiship.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <nav class="navbar navbar-toggleable-md navbar-light">
            <div class="container">
                <a class="navbar-brand" href="index.html">This Is Hip</a>
            </div>
        </nav>
    </div>

    <div class="container">
    \n"""
end_of_doc = """
    </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script>window.jQuery || document.write('<script src="js/vendor/jquery.min.js"><\/script>')</script>
    <script src="js/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="js/vendor/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
</body>\n"""

def event_link_html(event_id):
    event_link = "    <p><a href=\"view_event.html?event_id=" + event_id + "\"> "
    event_link += event_id + " </a></p>\n"
    return event_link

if __name__ == "__main__":
    list_of_events = os.listdir("../facebookeventjsondump/events/")
    events_html = ""
    for event in list_of_events:
        event_link = event_link_html(event.split('.')[0])
        events_html += event_link

    with open ("index.html",'w') as new_index:
        new_index.write(head_of_doc)
        new_index.write(events_html)
        new_index.write(end_of_doc)
    new_index.close()
