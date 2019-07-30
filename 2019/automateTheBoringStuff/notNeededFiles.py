#! python3

import os, sys

##################### USAGE #####################
# python notNeededFiles.py <path> walks through <path> 

##################### TODO #####################
# Walk through folder tree
# identify files with size larger than 100 MB
# print results

if len(sys.argv) == 3:
	if os.path.exists(sys.argv[1]):
		for foldername, subfolders, filenames in os.walk(sys.argv[1]):
			for folder in subfolders:
				if os.path.getsize(foldername + "/" + folder) > (int(sys.argv[2])):
					print(foldername + "/" + folder)

else:
	print('path/file size not entered not entered')

