#! python3

##################### TODO #####################
# Walk through folder tree
# identify files with user inputted extension
# copy all files with extension into a new folder

import os, shutil

cwd = input('enter location of dir to be walked through: ')
ext = input('enter file extension: ')
new = input('enter location of result dir: ')

if not os.path.exists(new):
	# make a result directory if doesn't already exist
	os.mkdir(new)

for foldername, subfolders, filenames in os.walk(cwd):
	for filename in filenames:
		if filename.endswith(ext):
			shutil.copy(foldername + '/' + filename, new)
			