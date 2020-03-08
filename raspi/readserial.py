import serial
import mysql.connector
import time;

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="waterme"
)

print(mydb)
mycursor = mydb.cursor()

serial = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1.0)
while True :
	time.sleep(5)
    try:
    	ts = time.time()
    	serial.flushInput()
      state = serial.readline()
      state = serial.readline().split(":")
      print(state[1])
      sql = "INSERT INTO zeitverlauf (timestamp, data) VALUES (%s, %s)"
		  val = (ts, state[1])
		  mycursor.execute(sql, val)
		  mydb.commit()
      if int(state[1]) < 500:
        serial.write("$")
        serial.flush()
        print("WATER!!!!!")
        pass
    except:
        pass