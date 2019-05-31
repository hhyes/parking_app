from serial import Serial
import subprocess
import time
from prediction import prediction
from db_management import search
arduino = Serial('/dev/ttyUSB2', 9600, timeout=.1)
plate=""
mutex=1
while True:
	data = arduino.readline() 
	if data:
		distanta=int(data)
		if (distanta < 10 and distanta >2):
			plate=""
			print data
			subprocess.call("./snap.sh", shell=True)
			time.sleep(1)
			plate=prediction()
			time.sleep(1)
			print plate
			if len(plate)>5:
				print search(plate)
				if(search(plate)==1)
					arduino.write(1)
