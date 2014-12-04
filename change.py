import subprocess
import sys
import fileinput

args={'make', 'clean'}
#subprocess.call(args)
args={'make'}
#subprocess.call(args)

# opens the file used for modification- file_1
file_1 = open(sys.argv[1])
write_line = ""

# iterate over each line in both the files
# iterate as many times as the parameters in file used for modification - file_1
for line_1 in file_1:
	
	# splits the line and creates a list
 	line_1_split =  line_1.split("=")
	# separate the text to be searched and text to be replaced
	search_text = line_1_split[0]
	replace_text= line_1_split[1]
	replace_text=replace_text.strip()

	
	# start looping from the beginning of the file to be modified file_2 for each line in file_1
	# for the above reason, the file has to be opened and closed again 
	#file_2 = open(sys.argv[2], "r+")
	file_3 = open(sys.argv[3], "a")
	#for line_2 in file_2:
	for line_2 in fileinput.input(sys.argv[2], inplace= 1):
		if search_text  in line_2:
			line_2_split = line_2.split("=")
			write_line =  line_2_split[0] + "= " + replace_text +";\n"
			seq = [line_2_split[0], "= ", replace_text, ";\n"]
			str = ""
			sp=str.join(seq)
			#pmerint write_line
			print sp,
			file_3.write(sp)
		else:
			print line_2,

	#file_2.close()


