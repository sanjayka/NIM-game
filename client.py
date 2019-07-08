import socket
import time
#creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to server
lost = "lost"
s.connect(('10.10.0.1', 8828)) # give your system ip address and select port number
# 172.16.6.1 is the server IP address 8888 is the port number shared
# sending 10 packets with 2 seconds gap
a = s.recv(100)
print(a.decode())
player = input()
s.send((player).encode())

a = s.recv(100)
print(a.decode())
st = s.recv(100)
print(st.decode())
x = 1;

while(x):

    st = s.recv(100)
    st = st.decode()
    print(st)
    if(lost in st):
        break
        s.close()
    if(player in st):
        print("Enter your move.")
        st = input()
        s.send((st).encode())
        st = s.recv(100)
        print(st.decode())

    st = s.recv(100)
    print(st.decode())

#closing connection
#s.close()
