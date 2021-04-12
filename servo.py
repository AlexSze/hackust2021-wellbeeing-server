from serial import Serial
from os import listdir
tty = "/dev/"
isLocked = True
s = 0
try:
	dev = listdir("/dev/")
	for device in dev:
		if "ttyUSB" in device:
			tty = tty + device
			break
	s = Serial(tty, 9600)
except:
	print("serial not found, testing mode")
def lock():
	global s
	if s != 0:
		s.write(b"1")
	isLocked = True

def unlock():
	global s
	if s != 0:
		s.write(b"2")
	isLocked = False
