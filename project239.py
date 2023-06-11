import hashlib 
import json
from time import time


chain=[]

def block(proof, previous_hash=None):
	transaction={
	"sender":"ronald",
	"recipient":"mcdonald",
	"amount":"5 ETH"
	}
	data={
	"index":1,
	"timestamp":time(),
	"transactions":transaction,
	"gas/fee":0.1,
	"block_reward":2.55,
	"uncle_reward":0,
	"difficulty":7317161775076869,
	"total_difficulty":28115205775076869,
	"size":"56528 bytes",
	"gas_used":14953987,
	"gas_limit":14955955
	"proof":proof,
	"previous_hash":previous_hash
	}
	chain.append(block)
	print("block information=",data)
	stringobject=json.dumps(data)
	block_string=stringobject.encode()
	rawhash=hashlib.sha512(block_string)
	hexhash=rawhash.hexdigest()
	print(hexhash)
block(previous_hash="no previous hash since this is the first block.", proof=000)



