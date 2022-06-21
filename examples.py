# Usage example

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

#================================================================================#

data = pd.read_csv("data.csv")
cs = data['FW']
clk = data['sym_pol']
mosi = data['Dch_ena']
miso = data['IFW']

datas = [cs, clk, mosi, miso]

with ExitStack() as stack:
	files = [stack.enter_context(open(fname, 'w')) for fname in fnames_event[:-1]]
	for f, d in zip(files, datas):
		print(f)
		for sample in d[start_index:end_index]:
			print(to_bin_str(sample, 1), file=f)
