from serial import Serial
from os import listdir
dev = listdir("/dev/")
tty = "/dev/"
for device in dev:
	if "ttyUSB" in device:
		tty = tty + device
		break
s = Serial(tty, 9600)
isLocked = True
def lock():
	global s
	s.write(b"1")
	isLocked = True

def unlock():
	global s
	s.write(b"2")
	isLocked = False
