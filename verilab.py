
#=======================================#
# Hardware evaluation helping programs
# Nikita Makarevich (a.k.a DDRDmakar)
# 2023
# dedrtos@gmail.com
#=======================================#

import numpy as np

# 7-segment code
# 7 bits:
# g f e d c b a
SS = [
	0x3F, # 0
	0x06, # 1
	0x5B, # 2
	0x4F, # 3
	0x66, # 4
	0x6D, # 5
	0x7D, # 6
	0x07, # 7
	0x7F, # 8
	0x6F, # 9
	0x77, # A
	0x7C, # b
	0x39, # C
	0x5E, # d
	0x79, # E
	0x71, # F
]

# Signed int to unsigned int
def to_uint(val, nbits):
	return val + 2**nbits if val < 0 else val

# Unsigned int to signed int
def to_sint(val, nbits):
	return val if val < 2**(nbits-1) else val - 2**nbits

# Int to binary string
def to_bin_str(val, width=None):
	if (width == None): return '{0:b}'.format(val)
	else:               return '{0:0{width}b}'.format(val, width=width)

# Int to hex string
def to_hex_str(val, width=None):
	if (width == None): return '{0:x}'.format(val)
	else:               return '{0:0{width}x}'.format(val, width=int(np.ceil(width/4)))

# Generate random signed int with given bit width
# If size != None, generate array of random values
def rand_sint_nbits(nbits, size=None):
	return np.random.randint(low=-(2**(nbits-1)), high=+(2**(nbits-1)), size=size)

# Generate random unsigned ints
# ----//----
def rand_uint_nbits(nbits, size=None):
	return np.random.randint(low=0, high=+(2**nbits), size=size)

# Encode data with manchester code
# input and output: numpy arrays of 0/1 values
# len(output) = 2 * len(input)
def manchester_encode(d):
	m = np.ndarray(len(d)*2, dtype=type(d[0]))
	pos = 0
	for b in d:
		if b:
			m[pos] = 1
			m[pos+1] = 0
		else:
			m[pos] = 0
			m[pos+1] = 1
		pos += 2
	return m

# Decode manchester code
# input and output: numpy arrays of 0/1 values
# len(input) = 2 * len(output)
def manchester_decode(m):
	d = np.ndarray(len(m)//2, dtype=type(m[0]))
	b2 = 0b00
	for i, b in enumerate(m):
		b2 = (b2 << 1) & 0b11 | b
		if i % 2:
			if b2 == 0b01: d[i // 2] = 0
			elif b2 == 0b10: d[i // 2] = 1
			else: break
	return d

# Shift elements in numpy arary
# returns shifted array
def shift_np_array(xs, n, cval=np.nan):
	e = np.empty_like(xs)
	if n >= 0:
		e[:n] = cval
		e[n:] = xs[:-n]
	else:
		e[n:] = cval
		e[:n] = xs[-n:]
	return e

# Encode int with corresponding gray code
def to_gray(x):
	return x ^ (x >> 1)

# Decode int from gray code
def from_gray(x):
	a = x
	mask = x
	while mask != 0:
		mask >>= 1
		a ^= mask
	return a

# Decode 8-bit alaw to 16-bit value
def from_alaw(x)
	xs = (x & 0x80) != 0; # sign
	xm = (x >> 4) & 0x07; # magnitude
	xf = (x & 0x0F) << 1 | 0x21; # fraction

	# Apply magnitude and sign
	if xm == 0:
		return -(xf & 0x001F) if xs else +(xf & 0x001F)
	else:
		return -(xf << xm) if xs else +(xf << xm)
