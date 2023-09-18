import os
import sys
import time
import socket

hn=socket.gethostname()
ip=socket.gethostbyname(hn)
log=hn,ip
lstr=':'.join(map(str,log))
ilpath="ips.txt"

def main():
    l=open("lgo.txt","r")
    lr=l.read()
    print(lr)

def ipcheck():
    with open(ilpath, "r") as file:
        text=file.read()
    if lstr in text:
        print("You are IP banned.")
        sys.exit()
    else:
        main()
ipcheck()