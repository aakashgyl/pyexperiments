#!/usr/bin/python

import sys
import getopt
import base64

from Crypto.PublicKey import RSA

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def decryptPassword(encrypted_passwd):
    pvt_enc_key = "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlDN0FJQkFBS0JvUURXVzBhdDdoaTZERkZRTDVqcjVOQWlZZ0M5K3I2dzBKWTZPZjlhMEdXeTZPQW1BbklICkFVM2hyN0w5WFM2bDcvbGhXb21tejJDc1EyR0FabGtqc01kcVdXVWRuNzdpOGJJOHludWxKREZjcWMyRFlySzUKZjZiQUlac1YvZS9CVUltRW5iM0ZtYkhtUks2d21LY3h5TFViSmdiV291dGxFZU03VVV6Sjl5NzhuNVo1WDhrNAovR1I2MHB3NTNyRGI2Qi9xNkpkc3JnWXZZWTlxRDJqbWpnNTlBZ01CQUFFQ2dhQmRWb2R6U3Y3M1hFKzM0OUhwCnZjdW5mUmNub2x5UWIzTkt6V0JVc2ZQbXNLS1J5blRPZWhIb21QSU9neG5CNWJtb1c1MGV4cVFvdm5waFI2KysKNjhZWmwrMkF0Y09QM0lDcEdkNDNMWWhVK1V0WDkzcGR3RC9yQjVYcitHYy92ODloL0pxbmk5UEFBSDdJTklCWQoyZGxGb3pTVXY5Q0E3QkVnK1F6OGJCeHdtQmhOTHc0WEV0ZDhTbWdrazZYdFFGbTdZeVc2cFpsS2Ird0FqeTIwCmN0VWRBbEVBNVljaU5ZMngwZmgwcWJJNTNRNzhLVm82Q29KazlOMTNld2wvWWhyRTlGUW8va1RUaFRSaEZ6NkkKSDNoV1R3TUc3ay9ZY1NuVGdXMFB0NUJlbHBKZW0yTDJNK2JJV2o5VWtTalFXeVdYRndNQ1VRRHZGRFNnWmIydgp5bk8xcURYVWRLdzFLVTNadnZhRjcreGVTT0o5T2QrYnlVb2xCRFBPbzhOV3l0eVhHVEV5MHJQN244ZFpKd3BtCks0QWc2UVArK05lZUl0YUJwaHUvakMxRUpxNmZEcXlNZndKUUN2Vmx1N3JWSjVvK0w2L3p0VXMyM042UzhOZUMKN0hINmQyUmZzWlpubXVhOXdrNFU3MEl0OUljbXhxSGZOUXlHOHkvYXZLUnJsYjFZUjhKYjBjS1JROGY0eTBlVQpmMEtRemhGdHlUeEZOM01DVVFDS3pKQkJEdEF4WHJnT25ybWh2cHE3d2w4UUsyMjBGTGFGaG9yM2FNSUpEN09jCkNmU0o0MGxrK2lGWEY2a1llSHRGZWwyaHhLaWs2RnhhdnUweStnVTBLY1dmUDNDY3BDVWppOUdWUmsrbXdRSlEKUklLR2ZsRGdSblRjRVoyT1ZnVWF4elgxbkpERlFVNXBNU2xRMWl6VXFROG4yTjk2SzRMRWRtSEFFYVZXMitWLwpRSG04d3VUejRRbnlIZEFQOHBjZWdkMzlIak54cHg0OHlKOEdVZUhVR2p3PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ=="
	pub_enc_key = "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHL01BMEdDU3FHU0liM0RRRUJBUVVBQTRHdEFEQ0JxUUtCb1FEV1cwYXQ3aGk2REZGUUw1anI1TkFpWWdDOQorcjZ3MEpZNk9mOWEwR1d5Nk9BbUFuSUhBVTNocjdMOVhTNmw3L2xoV29tbXoyQ3NRMkdBWmxranNNZHFXV1VkCm43N2k4Ykk4eW51bEpERmNxYzJEWXJLNWY2YkFJWnNWL2UvQlVJbUVuYjNGbWJIbVJLNndtS2N4eUxVYkpnYlcKb3V0bEVlTTdVVXpKOXk3OG41WjVYOGs0L0dSNjBwdzUzckRiNkIvcTZKZHNyZ1l2WVk5cUQyam1qZzU5QWdNQgpBQUU9Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="
    
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

 
