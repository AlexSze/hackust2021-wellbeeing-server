from serial import Serial
from os import listdir

tty = "/dev/"
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

# return True if success
def lock():
	global s
	if s != 0:
		s.write(b"1")
		return True
	else:		# no servo is connected
		return False

# return True if success
def unlock():
	global s
	if s != 0:		
		s.write(b"2")
		return True
	else:		# no servo is connect
		return False
