# USAGE
# python transform_m.py images/example_01.png "[(73, 239), (356, 117), (475, 265), (187, 443)]"
# python transform_m.py images/example_02.png "[(101, 185), (393, 151), (479, 323), (187, 441)]"
# python transform_m.py images/example_03.png "[(63, 242), (291, 110), (361, 252), (78, 386)]"


# Standard library
import argparse

# 3rd-party library
import numpy as np
import cv2

# My library
from utilities.transform import four_point_transform

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser(description='Transforming image from any shape to rectangle')
parser.add_argument('image',metavar='IMG', help='Path to Image file')
parser.add_argument('coords', metavar='COQ', help='Cordinates of 4 corners of given quadrilateral')

args = vars(parser.parse_args())

# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype = "float32")

# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)

# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)

