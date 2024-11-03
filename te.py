import serial
import os
import requests
import time
#ser = serial.Serial('COM4', 115200)  # Adjust port and baud rate
ser = serial.Serial('COM3', 115200)
suid = ""
url = 'http://127.0.0.1:8000/api/person/'

# Data to be sent in the POST request (this is just an example)

try:
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            print(data)
            if data == "RFID UID:  43 67 C1 17":# workingMessage : Authorized access":
                print("open")
                print(data)
                suid =data
                data2 = {
                    'id':data,
                    'name': data,
                    'age': 22
                }
                os.startfile("desg.py")
                response = requests.post(url, json=data2)
                print(response.text)

            #requests.post(suid)
            else:
                print(data)
                suid = data
                data2 = {
                    'id':data,
                    'name': data,
                    'age': 22
                }
                os.startfile("desg.py")
                response = requests.post(url, json=data2)
        except:
            continue
finally:
    ser.close()
            
            
