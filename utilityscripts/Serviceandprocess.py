import psutil
import os

def returnhtmlfragment(c1, c2, c3):
    return f'<tr><td>{c1}</td><td>{c2}</td><td>{c3}</td></tr> \n'

def changehtmltdcolor(actual, expected, condition):
    color = "red"
    if condition == '==':
        if actual == expected:
            color = "green"
    if condition == '<':
        if actual < expected:
            color = "green"

    return f'<td bgcolor = "{color}">{actual}</td>'



file = open("sample.html", "w")
op = ''
for proc in psutil.process_iter():
    processName = proc.name()
    processId = proc.pid
    mem = proc.memory_percent()
    op += f'<tr><td>{processName}</td><td>{processId}</td>{changehtmltdcolor(round(mem,2), 1, "<")}</tr> \n'



sv = ''
for serv in psutil.win_service_iter():
    serviceName = serv.name()
    serviceExe = serv.binpath()
    status = serv.status()
    sv += f'<tr><td>{serviceName}</td>{changehtmltdcolor(status,"running", "==")}<td>{serviceExe}</td></tr> \n'




newop = f'''
<h>Process details</h>
<table border=3>
<th>name</th><th>pid</th><th>memory%</th>
{op}
</table>
</br>
<h>Service details</h>
<table border=3>
<th>name</th><th>status</th><th>command</th>
{sv}
</table>
'''
file.write(newop)
file.close()

# proc = psutil.process_iter()
# proc.
# print(proc[1])
