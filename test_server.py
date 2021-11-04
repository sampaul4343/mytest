import socket
import threading


class Client(threading.Thread):
  def __init__(self, conn, addr):
    threading.Thread.__init__(self, daemon = True)
    self.__conn = conn
    self.__addr = addr
    print("come from: {}".format(addr))
    
   
  
  def run(self):
    try:
      while True:
        data = self.__conn.recv(1024)
        self.__conn.sendall(data)
    except Exception as e:
      print(e)
    self.__conn.close()
    
    
    
port = 5000
sck = socket.socket()
sck.bind(('', port))
sck.listen(5)



try:
  while True:
    conn, addr = sck.accept()
    Client(conn, addr).start()
except Exception as e:
  print(e)

  
sck.close()
