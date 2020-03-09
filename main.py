#!/usr/bin/python36
print("content-type: text/html")
print()
import subprocess
dockerlist = "docker container ls -a"
dockerlistoutput = subprocess.getoutput(dockerlist)
container_list = dockerlistoutput.split("\n")

#print("<iframe width='100%' name='myconsole'></iframe>")
print("""
<table border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
</tr>""")

for c in container_list[1:]:
	if "Up" in c:
		cstatus = "running"
	elif  "Exited" in c:
		cstatus = "stopped"
	else:
		status = "unknown status"
	c_details  =  c.split()
	cname =  c_details[-1]
	imagename = c_details[1]
	print('''
	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.50/cgi-bin/dockerportal/dockerstart.py?s={}'>Start</a></td>
	<td><a href='http://192.168.43.50/cgi-bin/dockerportal/dockerstop.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.43.50/cgi-bin/dockerportal/dockerterminate.py?s={}'>Terminate</a></td>
	</tr>
	'''.format(cname, imagename, cstatus, cname, cname, cname ))

print("</table>")
