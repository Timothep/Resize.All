import os
import glob

def PrintAllFiles(files):
	print "All files found:"
	for file in files:
			print file

def DiscoverPaths(rootPath, recursive, extensions, verbose = False):
	files_grabbed = []
	if recursive:
		for root, subdirs, files in os.walk(rootPath):
		    for file in files:
		        if os.path.splitext(file)[1].lower() in extensions:
					files_grabbed.append(os.path.join(root, file))
	else:
		for extension in extensions:
			files_grabbed.extend(glob.glob(rootPath + "/*" + extension))
	
	if verbose:
		PrintAllFiles(files_grabbed)

	return files_grabbed