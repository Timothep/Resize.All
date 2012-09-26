# About #

Resize.me is a simple Python script used to resize all the images present in a folder (and eventually in its subfolders)

# Usage #
* -h, --help            					show this help message and exit
* -s SIZE, --size SIZE  					The size of the longest border of the image after resizing
* -p PATH, --path PATH  					The root path in which to search for images
* -r, --recursive       					A flag defining whether the files are to be searched in every subdirectory (False per defaul)
* -o, --overwrite       					A flag defining whether the files are to be overwritten or new files to be created alongside (False per default)
* -v, --verbose         					Printout statements along the way (False per default)

# Example #

Resizing all the '.jpg' and '.png' images present in 'C:\temp' and its subdirectories, overwriting the original images and printing extended information along the way

```python
python -s 1024 -p C:\temp -o -v -r
```

# Dependencies #
- Python 2.7
- Python Image Library (PIL) 1.1.7