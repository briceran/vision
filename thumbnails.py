from PIL import Image
import os
""""generates thumbnails from a provided list of jpg filenames"""

def make_thumbnails(imagepathlist):
    size = 128, 128    
    for infile in imagepathlist:
        file, ext = os.path.splitext(infile)
        try: 
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(file + ".thumbnail", "JPEG")
        except IOerror:
            print ("can't convert", infile)