import serial
import os
ser = serial.Serial('COM3', 115200)  # Adjust port and baud rate
t = []
s = 0
os.startfile("C:\\Users\\Shivash\\Documents\\Hackathon\\des2.py")
try:
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(data)
        t.append(data)
        tt = str(t)
        s = s+1
        while s%100==0:
            with open ("resultsdes.txt","w") as f:
                f.write(tt)
            t.clear()
            break


finally:
    ser.close()