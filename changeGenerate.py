fileText = open('myChange.txt','w')

cta_size_range = [32, 64, 128, 256, 512, 1024]

for cta_size_num in cta_size_range:
	fileText.write('CTA_SIZE = '+ str(cta_size_num)+'\n')
	fileText.write('WARP_SIZE = 32\n')
	fileText.write('__items_per_thread = 7\n')
	fileText.write('__num_ctas = 1* (1 << 10)\n\n')
