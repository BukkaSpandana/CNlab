import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',2222))
s.listen(5)
client,address=s.accept()
n=client.recv(1024)
enc=[]
data=client.recv(1024)
for k in data:
	l=ord(k)
	c=1
	for m in range(0,int(e)):
		c*=l
		c%=n
	c%=n
	enc.append(c)
s.send(enc)
