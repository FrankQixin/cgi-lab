#!/usr/bin/env python3
import json, os
print("Content-type:text/html\r\n\r\n")
print("<title>Testing CGI</title>")


#Lab code 

# Q1
print(os.environ)
json_object = json.dumps(dict(os.environ))
print(json_object)


# Q2

for param in os.environ.keys():
  if param == "QUERY_STRING":
    print("<b>%20s</b>: %s<br>".format(param, os.environ[param]))

# Q3

for param in os.environ.keys():
  if param == "HTTP_USER_AGENT":
    print("<b>%20s</b>: %s<br>".format(param, os.environ[param]))