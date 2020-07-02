import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.255.255.255', 1))
print('Your IP address is', s.getsockname()[0])
s.close()
