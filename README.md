# Resize.All #

Resize.me is a simple Python script used to resize all the images present in a folder (and eventually in its subfolders)
Currently supported are .jpg, .jpeg & .png files.

### Usage ###
* -h, --help            					show the help message and exit
* -s SIZE, --size SIZE  					The size of the longest border of the image after resizing (mandatory)
* -p PATH, --path PATH  					The root path in which to search for images (mandatory)
* -r, --recursive       					A flag defining whether the files are to be searched in every subdirectory (False per default)
* -o, --overwrite       					A flag defining whether the files are to be overwritten or new files to be created alongside (False per default)
* -v, --verbose         					Printout statements along the way (False per default)

### Example ###

Resizing all the images present in 'C:\temp' and its subdirectories, overwriting the original images and printing extended information along the way

```python
python Resize.All.py -s 1024 -p C:\temp -o -v -r
```

## Dependencies ##
- Python 2.7 -> http://www.python.org/
- Python Image Library (PIL) 1.1.7 -> http://www.pythonware.com/products/pil/

# Open Issues / Further Developments #
* Add the ability to provide extensions via arguments
* Resize one image only
* Create Unit Tests