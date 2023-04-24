import socket

s = socket.socket()

port = 3000

s.bind(('127.0.0.1',port))

s.listen(5)

msg = str.encode("Thanks For Connecting")

while True:
   c,addr = s.accept()
   print("connected to address: ",addr)
   c.send(msg)
   c.close()
