import os
from datetime import datetime
button_id='AAPL'
f = open("static/images/"+button_id+"/low_date.txt", "r")
date_object = datetime.strptime(f.read()[:10], '%Y-%m-%d')
print(date_object)