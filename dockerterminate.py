#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")


form = cgi.FieldStorage()

cname = form.getvalue("s")

cmd = "docker rm -f {}".format(cname)

x = subprocess.getoutput(cmd)

print("location: http://192.168.43.50/cgi-bin/dockerportal/main.py")
print()

