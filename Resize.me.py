import os, sys
import Image
import glob
import argparse
from FilesCrawler import DiscoverPaths
from ImageManipulation import ResizeImage

def ResizeImages(allImages, size, overwrite):
	for image in allImages:
		ResizeImage(image, size, overwrite, verbose)

def GetArgumentOrDefault(argumentName, defaultValue = None):
	return args[argumentName] if args[argumentName] != None else defaultValue

# Some predefined values
recursive = False
overwrite = False
verbose = False
extensions = ['.jpg', '.png', '.jpeg', '.gif']

# Argument parsing
parser = argparse.ArgumentParser(description='Resize.me is a script used to resize a batch of images.')
parser.add_argument('-s','--size', help='The size of the longest border of the image after resizing', required=True)
parser.add_argument('-p','--path', help='The root path in which to search for images', required=True)
#parser.add_argument('-e','--extensions', nargs='+', type=str, help='The extensions that should be analyzed, (' + str(extensions) + ' per default)' , required=False)
# Flags parsing
parser.add_argument('-r','--recursive', action='store_true', help='A flag defining whether the files are to be searched in every subdirectory (' + str(recursive) + ' per default)', required=False)
parser.add_argument('-o','--overwrite', action='store_true', help='A flag defining whether the files are to be overwritten or new files to be created alongside (' + str(overwrite) + ' per default)', required=False)
parser.add_argument('-v','--verbose', action='store_true', help='Printout statements along the way (' + str(verbose) + ' per default)', required=False)

args = vars(parser.parse_args())

size = GetArgumentOrDefault("size")
rootPath = GetArgumentOrDefault("path")
recursive = GetArgumentOrDefault("recursive", recursive)
overwrite = GetArgumentOrDefault("overwrite", overwrite)
verbose = GetArgumentOrDefault("verbose", verbose)

# Discovering the images to resize
print extensions
allImages = DiscoverPaths(rootPath, recursive, extensions, verbose)

# Resizing the images
#ResizeImages(allImages, size, overwrite)