from datetime import datetime
import os
import glob
button_id='AAPL'
if not os.path.exists('static/images/'+button_id):
    os.makedirs('static/images/'+button_id)
    text_file = open("static/images/"+button_id+"/time.txt", "w")
    text_file.write(datetime.now().strftime("%Y-%m-%d"))
    text_file.close()
else:
    f = open("static/images/"+button_id+"/time.txt", "r")
    date_object = datetime.strptime(f.read(), '%Y-%m-%d')
    if date_object.date()<datetime.now().date():
      try:
        files = glob.glob('static/images/'+button_id+'/*')
        for f in files:
         os.remove(f)
        text_file = open("static/images/"+button_id+"/time.txt", "w")
        text_file.write(datetime.now().strftime("%Y-%m-%d"))
        text_file.close()
      except Exception as e:
        print('Reason: %s' % (e))
      print("data reload needed")
    else:
     print("not needed")