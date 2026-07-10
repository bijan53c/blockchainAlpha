import json
import requests
from time import time
from uuid import uuid4
import hashlib

def WalletCreate():
	'''Creates a wallet file if it doesn't exist'''
	private_key = rsa.generate_private_key(
	        public_exponent=65537,
	        key_size=2048,
	        backend=default_backend()
	)
	## Shows private key importance
	input("Private key file got created in wallet's directory, keep it safe\n That's the only way back to data of this wallet.\n For using this wallet on other devices you'll need to move the file or data in it.\n >> By pressing the enter you confirm that you understand the importance and accept this message<<")
	
	public_key = private_key.public_key()

	## Saving keys to files
	PRVkey = open("prv","w")
	PRVkey.write(private_key)
	PRVkey.close()

	Pubkey = open("pub","w")
	Pubkey.write(public_key)
	PubKey.close()


	input ("Your wallet got created!\n>> Press ENTER to acknowledge")





def WalletLogin():
	'''Logins to wallet if one already exists with provided password'''	
	'''++ We can add decrypt on successful logon here++'''
	PrvKey = open("prv","r")
	private_key = PrvKey.read()
	PrvKey.close()

	PubKey = opne("pub","r")
	public_key = PubKey.read()
	PubKey.clos()


def UpDate():
	'''Gets latest blockchain data to update wallet balance'''
	''' using fullchain request'''



def SendTransac():
	'''Send amounts of crypto to an address'''
	pass

def GetTransac():
	'''Shows address for receiving crypto from someone else'''
	pass




