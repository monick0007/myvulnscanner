from os import system
import subprocess

import wexpect
import csv
access_keyID=''
access_secret=''
def awsconf():
    try:
        with open('new_user_credentials.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if row[0]=='User name':
                    continue
                else:
                    access_keyID=row[2]
                    access_secret=row[3]
                    region=row[5]
                    username=row[0]
    except:
        print('please download csv file of iam user in this diretory')                
        system.exit(0)
    child = wexpect.spawn('cmd.exe')
    child.expect('>')
    child.sendline('aws configure')
    child.expect(':')
    child.sendline(access_keyID)
    child.expect(':')
    child.sendline(access_secret)
    child.expect(':')
    child.sendline(region)
    child.expect(':')
    child.sendline(region)
    child.expect(':')
    child.sendline('html')
    child.expect('>')
    print(child.before)
    print('setup successful with '+username)
    print('closing program and opening the html report....')

