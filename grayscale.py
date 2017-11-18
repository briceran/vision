from PIL import Image
import os
import imtools
import imtools

im_paths = imtools.get_imlist(os.getcwd())


im1 = Image.open(im_paths[0])
im2 = Image.open(im_paths[1])

#grayscale

im1_gs = im1.convert('L')
im2_gs = im2.convert('L')

for infile in im_paths:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try: 
            Image.open(infile).save(outfile)
        except IOerror:
            print ("can't convert", infile)