import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',2222))
p=input("enter p: ")
q=input("Enter q: ")
e=raw_input("Enter e ,co-prime to p-1 X q-1: ")
s.send(e)
d=1
s=0
n=p*q
phi=(p-1)*(q-1)
ec=int(e)
while(s!=1):
	s=(d*ec)%phi
	d+=1
d-=1
data=raw_input("Enter data: ")
s.send(data)
enc=s.recv(1024)		
print "decrypted: "
dec=[]
for k in enc:
	c=1
	for l in range(0,d):
		c*=k
		c%=n
	c%=n
	dec.append(chr(c))
#print dec
str=' '
for k in dec:
	str+=k
print str[1:]
