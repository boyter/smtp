import socket
import sys  

remote_ip = '127.0.0.1'
port = 2525

print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Connecting to server, (' + remote_ip + ')')
s.connect((remote_ip , port))

print('# Sending data to server')
request = "aiufbasoufbnasdfg"

try:
    s.sendall(request)
except socket.error:
    print 'Send failed'
    sys.exit()

print('# Receive data from server')
reply = s.recv(4096)

print reply 