import subprocess
import sys
import fileinput
import os

# opens the file used for modification- file_1
file_1 = open(sys.argv[1])


# iterate over each line in both the files
# iterate as many times as the parameters in file used for modification - file_1
for line_1 in file_1:
	if  line_1.strip()=="": continue
	else:
		# splits the line and creates a list
 		line_1_split =  line_1.split("=")
		length = len(line_1_split)	
		
		# separate the text to be searched and text to be replaced
		search_text = line_1_split[0]
		replace_text= line_1_split[1]
		replace_text=replace_text.strip()

		# start looping from the beginning of the file to be modified file_2 for each line in file_1
		# for the above reason, the file has to be opened and closed again 
		for line_2 in fileinput.input(sys.argv[2], inplace= 1):
			if search_text  in line_2:
				line_2_split = line_2.split("=")
				seq = [line_2_split[0], "= ", replace_text, ";\n"]
				str = ""
				sp=str.join(seq)
				print sp,
			else:
				print line_2,

		if line_1.startswith('__num_ctas'):
			args= {'make', 'clean'}
			subprocess.call(args)
			args={'make'}
			subprocess.call(args)
			subprocess.check_call(["./spmv", "Williams/cant.mtx"])
			
file_1.close()


