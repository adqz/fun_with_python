import socket

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)

while True:
  clt, adr = s.accept()
  print(f'Connection to {adr} established')
  # pass message from server to client
  clt.send(bytes('socket prog in python', 'utf-8'))