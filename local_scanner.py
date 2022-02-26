from tkinter import W
import os
import subprocess
def localscan():
    # sc=nmap.PortScanner()
    # a=os.system("nmap -p 1-5000 -sV --script vuln 127.0.0.1")
    a=subprocess.getoutput('nmap -p 1-5000 -sV --script vuln 127.0.0.1')
    # a=sc.scan('127.0.0.1','1-500')

    with open('localoutput.txt','w') as data:
        data.writelines(a)