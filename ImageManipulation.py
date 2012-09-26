import Image
import os

def ResizeImage(imagePath, size, overwrite, verbose = False):
	if verbose:
		print "Resizing image " + imagePath

	extension = os.path.splitext(imagePath)[1][1:]
	try:
		im = Image.open(imagePath)
		
		oldSize = im.size

		im.thumbnail((int(size), int(size)), Image.ANTIALIAS)

		if verbose:
			print "Image size: " + str(oldSize) + " => " + str(im.size)

		if overwrite:
			im.save(imagePath, im.format)
		else:
			newName = os.path.splitext(imagePath)[0] + "_" + str(size) + os.path.splitext(imagePath)[1]
			im.save(newName, im.format)
	except IOError:
		print "Cannot create thumbnail for '%s'" % imagePath