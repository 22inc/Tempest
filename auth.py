import os
import sys
import time
import socket

hn=socket.gethostname()
ip=socket.gethostbyname(hn)
log=hn,ip
lstr=':'.join(map(str,log))
ilpath="ips.txt"

def ipcheck():
    with open(ilpath, "r") as file:
        text=file.read()
    if lstr in text:
        print("You are IP banned.")
        sys.exit()
ipcheck()

usr=input("Name? ")
psw=input("Phrase? ")
login=usr,psw
db=open("usrs.txt","r")
        
def check(usr,psw):
    with open("usrs.txt","r") as db:
        for line in db:
            parts=line.strip().split(":")
            if len(parts)==3:
                susr,spsw,con=parts
                if usr==susr and psw==spsw:
                    print(f"You are {con}.")
                    time.sleep(1)
                    os.system('cls')
                    os.system('python main.py')
                    return
                else:
                    os.system('clear')
                    os.system('cls')
                    print(lstr)
                    with open('ips.txt','a') as file:
                        file.write(lstr+'\n')
                        time.sleep(1)
                        time.sleep(2.5)
                        sys.exit()
check(usr,psw)