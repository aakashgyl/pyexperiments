#!/usr/bin/python

import os
import sys
import getopt
import base64

from Crypto.PublicKey import RSA
from Crypto import Random
import getpass

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def checkFileExist(file_path):
    '''Checks if file exists'''
    if not os.path.isfile(file_path):
        return False
    else:
        return True

def encryptPassword(passwd):
    keypair =  RSA.importKey(base64.b64decode(pub_enc_key))

    pubkey  = keypair.publickey()
    encrypted_passwd_tuple   = pubkey.encrypt(pad(passwd), 32)
    
    #encode the first string in tuple to avoid '#' in output
    encrypted_passwd = base64.b64encode(str(encrypted_passwd_tuple[0]))
    print encrypted_passwd
    #print type(encrypted_passwd), len(encrypted_passwd)
        
def errorMsg(val):
    print "\nInvalid input\n"
    sys.exit(2)

def getPassword():
    print "Enter details asked below: "
    return getpass.getpass()

def validateCliInput():
    version = "encryptPassword.py 1.0"
    
    if len(sys.argv) == 1:
        passwd = getPassword()
        encryptPassword(passwd)
        
    elif len(sys.argv) in [2,3] :
        try:
            opts, _ = getopt.getopt(sys.argv[1:],"hp:",["help"])
        except getopt.GetoptError:
            errorMsg(sys.argv)
        
        for opt, arg in opts:
            if len(sys.argv) == 2:
                if opt in ("-h","--help"):
                    sys.exit(0)
                elif opt in ('-v') :
                    print "\nVersion : %s\n" %(version)
                    sys.exit(0)
            elif len(sys.argv) == 3:
                if opt in ('-p'):
                    encryptPassword(arg)
            else:
                errorMsg(sys.argv)
    else:
        errorMsg(sys.argv)

if __name__ == '__main__':
    validateCliInput()

 
