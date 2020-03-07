import serial
serial = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1.0)
while True :
    try:
        state=serial.readline()
        print(state)
    except:
        pass