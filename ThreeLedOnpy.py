#!/usr/bin/python37all
# put this file in /usr/lib/cgi-bin/
# and change permissions (sudo chmod 755 led.py)

import RPi.GPIO as GPIO
import cgi
import cgitb # optional, for better exception handling
cgitb.enable()   # optional

ledPin1 = 19
ledPin2 = 16
ledPin3 = 12

GPIO.setmode(GPIO.BCM) # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

# Begin generation of web page showing current state:
print ('Content-type:text/html\n\n') # blank line = end of headers
print ('<html> Choose Which LED you want on')
print ('<head>')
print ('<title>LED switch test</title>')
print ('<meta http-equiv="refresh" content="30">') # update every 30 sec
print ('</head>')
print ('<body>')
print ('<div style="width:600px;background:#AAAAFF;border:1px;text-
align:center">')
print ('<br>')
print ('<font size="3" color="black" face="helvetica">')
print ('<b>LED switch</b>')
print ('<br><br>')

# look at POST data for either 'on' or 'off' button names, using 
# "if ('on' in form)" instead of data.getvalue() since we have 2 different
# button names (unlike prior example with a single button name & 2 values):

form = cgi.FieldStorage()  # get POST data

if ('on1' in form):
  GPIO.output(ledPin1, 1)
elif ('off1' in form):
  GPIO.output(ledPin1, 0)

if ('on2' in form):
  GPIO.output(ledPin2, 1)
elif ('off2' in form):
  GPIO.output(ledPin2, 0)

if ('on3' in form):
  GPIO.output(ledPin3, 1)
elif ('off3' in form):
  GPIO.output(ledPin3, 0)

# display current LED state to user:
if GPIO.input(ledPin1):
  print ('<font color="red"> LED1 IS ON')
else:
  print ('<font color="black"> LED1 IS OFF')
  print ('<font color="black">')
  print ('<br><br>')

if GPIO.input(ledPin2):
  print ('<font color="red"> LED2 IS ON')
else:
  print ('<font color="black"> LED2 IS OFF')
  print ('<font color="black">')
  print ('<br><br>')

if GPIO.input(ledPin3):
  print ('<font color="red"> LED3 IS ON')
else:
  print ('<font color="black"> LED3 IS OFF')
  print ('<font color="black">')
  print ('<br><br>')

# Create the buttons to change LED state. Use 'target="_blank"
# to open in a new window if desired:
print ('<form action="/cgi-bin/ThreeLedOnpy.py" method="POST" target="_self">')
print('<input type = "submit" name="on1" value="Turn LED1 on">')
print('<input type = "submit" name="off1" value="Turn LED1 off">')
print('<input type = "submit" name="on2" value="Turn LED2 on">')
print('<input type = "submit" name="off2" value="Turn LED2 off">') 
print('<input type = "submit" name="on3" value="Turn LED3 on">')
print('<input type = "submit" name="off3" value="Turn LED3 off">')
print ('</form>')
print ('<br>')
print ('</body>')
print ('</html>')