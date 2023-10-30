# Usage example

from contextlib import ExitStack

from verilab import *

#========[ Generate dataset for testing HDL module sorting 4 numbers ]========#

fnames = [
	'D0.dat',
	'D1.dat',
	'D2.dat',
	'D3.dat',
	'RES0.dat',
	'RES1.dat',
	'RES2.dat',
	'RES3.dat',
]

with ExitStack() as stack:
	files = [stack.enter_context(open(fname, 'w')) for fname in fnames]
	
	for i in range(256):
		N = 16
		D = rand_uint_nbits(N, size=4)
		RES = np.sort(D)
		
		print(to_bin_str(D[0], N), file=files[0])
		print(to_bin_str(D[1], N), file=files[1])
		print(to_bin_str(D[2], N), file=files[2])
		print(to_bin_str(D[3], N), file=files[3])
		
		print(to_bin_str(RES[0], N), file=files[4])
		print(to_bin_str(RES[1], N), file=files[5])
		print(to_bin_str(RES[2], N), file=files[6])
		print(to_bin_str(RES[3], N), file=files[7])


#========[ Example reading CSV file with pandas ]========#
# 
# data = pd.read_csv("data.csv")
# a = data['FW']
# b = data['sym_pol']


#========[ Other ]========#

print('to_uint')
for e in [to_uint(i, 8) for i in [-4, 4]]:
	print(to_hex_str(e, 8), to_bin_str(e, 8))

print('to_sint')
for e in [to_sint(i, 8) for i in [252, 253, 254, 255, 0, 1, 2, 3]]:
	print(to_hex_str(e, 8), to_bin_str(e, 8))

print('rand_sint_nbits')
print(rand_sint_nbits(4, 10))

print('rand_uint_nbits')
print(rand_uint_nbits(4, 10))

print('manchester_encode')
b = np.random.randint(0, 2, 20, dtype=np.int8)
m = manchester_encode(b)
print(b)
print(m)

print('manchester_decode')
b2 = manchester_decode(m)
print(b2)

print('to_gray')
for e in [to_gray(i) for i in range(10)]:
	print(to_hex_str(e, 8), to_bin_str(e, 4))
print('from_gray')
for e in [from_gray(i) for i in range(10)]:
	print(to_hex_str(e, 8), to_bin_str(e, 4))
