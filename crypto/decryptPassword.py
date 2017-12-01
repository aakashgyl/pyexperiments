#!/usr/bin/python

import sys
import getopt
import base64

from Crypto.PublicKey import RSA

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def decryptPassword(encrypted_passwd):
    #import private key, decode and make into tuple, decrypt and unpad
    keypair_pvt = RSA.importKey(base64.b64decode(pvt_enc_key))
    decrypt_passwd_tuple = ((base64.b64decode(encrypted_passwd),))
    decrypted_passwd   = unpad(keypair_pvt.decrypt(decrypt_passwd_tuple))
    print decrypted_passwd

    
def errorMsg(val):
    print "\nInvalid input\n"
    sys.exit(2)

def validateCliInput():
    version = "decryptPassword.py 1.0"
    if len(sys.argv) in [2,3] :
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
                    decryptPassword(arg)
            else:
                errorMsg(sys.argv)
    else:
        errorMsg(sys.argv)

if __name__ == '__main__':
    validateCliInput()

 
