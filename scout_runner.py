from socket import timeout
import time
import wexpect
import subprocess
from aws_setup import awsconf

def scoutrun():
#coment out line no 5 if you're running the code for the first time
    subprocess.getoutput('rmdir /Q /S scoutsuite-report')

    #this method sets up aws with credentials stored in csv file
    awsconf()

    #scouting intitiated
    next = wexpect.spawn('cmd.exe')
    next.expect('>')
    next.sendline('scout aws')
    time.sleep(30)

