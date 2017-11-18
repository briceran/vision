import os 
"""Returns a list of filenames for all jpg images in a directory. """

def get_imlist(path): 
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('JPG')]
 