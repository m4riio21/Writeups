#!/usr/bin/python3
import os
from pwn import xor
def main():
	partly_plaintext = b'HTB{'
	cipher = bytes.fromhex('134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9')
	key = xor(partly_plaintext,cipher)[0:4]

	print('\n PLAIN:', xor(cipher,key))
	
if __name__ == '__main__':
    main()
