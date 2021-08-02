#!/usr/bin/python3
from Crypto.Util.number import getPrime, long_to_bytes, inverse, bytes_to_long

def decrypt(data):
	res = b'AAA'
	while b'HTB' not in res:
		p = getPrime(512)
		q = getPrime(512)
		d = inverse(3, (p-1)*(q-1))
		n = p*q
		pt = pow(data, d, n)
		new_data = long_to_bytes(pt)
		if b'HTB' in new_data:
			res = new_data

	print(res)


cipher = '05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965'

cipher = bytes.fromhex(cipher)
cipher = bytes_to_long(cipher)

decrypt(cipher)
