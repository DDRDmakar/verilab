
import numpy as np
from contextlib import ExitStack

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

def rand_sint_nbits(nbits, size=None):
	np.random.randint(low=-(2**(nbits-1)), high=+(2**(nbits-1)), size=size)

def rand_uint_nbits(nbits, size=None):
	np.random.randint(low=0, high=+(2**nbits), size=size)
