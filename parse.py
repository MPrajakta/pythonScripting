import sys
# open the file to parse
file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2],"w+a")
for line in file_1:
	if line.strip()=="":
		continue
	else:
		if line.startswith("csr_scalar_tex") or line.startswith("csr_vector_tex") or line.startswith("coo_tex") or line.startswith("ell"):
			line_split = line.split()
			seq = [line_split[0], "\t", line_split[4], "\n"]
			str  = ""
			sp = str.join(seq)
			file_2.write(sp)
file_2.close()
file_1.close()
