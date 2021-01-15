import imageio
from PIL import Image
from exifRotations import *

def saveVideoFromImage(imgId):
    im = Image.open("images/" + imgId+".png")
    im = apply_orientation(im)
    images = []
    width, height = im.size 
    print(width, height)
    # to get that instagram full screen good-good, use 9/16
    aspect_ratio = 9/16
    width_out = round(aspect_ratio * height)
    print(width_out, height)
    left = 0
    top = 0
    right = width_out
    bottom = height
    frame_increment = 60 # horizontal pixels to move per frame
    fps = 30
    pause_amt = 1 # seconds
    #pause at the beginning
    im1 = im.crop((left, top, right, bottom))
    images.extend([im1]*round(fps*pause_amt))
    while right < width:
        im1 = im.crop((left, top, right, bottom))
        images.append(im1)
        left += frame_increment
        right += frame_increment
    right -= frame_increment
    left -= frame_increment
    #pause at right side
    im1 = im.crop((left, top, right, bottom))
    images.extend([im1]*round(fps*pause_amt))
    while left > 0:
        im1 = im.crop((left, top, right, bottom))
        images.append(im1)
        left -= frame_increment
        right -= frame_increment
    left = 0
    top = 0
    right = width_out
    bottom = height
    im1 = im.crop((left, top, right, bottom))
    #pause at the beginning again
    images.extend([im1]*round(fps*pause_amt))
    imageio.mimsave("./videos/" + imgId + ".mp4", images, fps=fps)
