import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1024)) #(adress, port nunber)

msg = s.recv(1024) #no. of bytes we want to recieve from server)
print(msg.decode('utf-8'))