import cv2
import numpy as np
import argparse

# Starting point of the script
# =======================================

if __name__ == '__main__':

    # Initialize ArgumentParser object to handle command line input
    parser = argparse.ArgumentParser(description="Image Processing tool to produce Harris visualizations")
    parser.add_argument("--path", help="Path to the image", default = 'kandinsky.jpg')
    parser.add_argument("--threshold", help="Indicates the threshold to detect corners", default="0.01")

    # Parse command line arguments and store them in args.
    args = parser.parse_args()

    filename = args.path
    threshold = float(args.threshold)

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>threshold*dst.max()]=[0,0,255]

    cv2.imshow('out',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
