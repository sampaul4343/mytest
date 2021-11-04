import socket
import threading
import datetime



host = "localhost"
port = 5000
cln = socket.socket()
cln.connect((host, port))
print("connected")



try:
  while True:
    text = input("> ")
    cln.sendall(text.encode("utf-8"))
    rev = cln.recv(1024).decode("utf-8")
    print(rev)
    print(datetime.datetime.now())
except Exception as e:
  print(e)

  
  
cln.close()
