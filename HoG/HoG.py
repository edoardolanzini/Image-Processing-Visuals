import cv2
import numpy as np
from skimage import feature
from skimage import exposure
import argparse

# Starting point of the script
# =======================================

if __name__ == '__main__':

    # Initialize ArgumentParser object to handle command line input
    parser = argparse.ArgumentParser(description="Image Processing tool to produce HoG visualizations")
    parser.add_argument("path", help="Path to the image")
    parser.add_argument("--ratio", help="Indicates the ratio of the resizing of the produced image", default="1")
    
    # Parse command line arguments and store them in args.
    args = parser.parse_args()

    # Path to image
    path = args.path

    # Ratio of resizing
    ratio = int(args.ratio)

    #Read image
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (img.shape[1]//ratio,img.shape[0]//ratio))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.float32(img) / 255.0

    # Extract Histogram of Oriented Gradients from the image
    (H, hog_img) = feature.hog(img, orientations=9, pixels_per_cell=(10, 10),
        cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1", visualize=True)

    # Visualize the HOG image
    hog_img = exposure.rescale_intensity(hog_img, out_range=(0, 255))
    hog_img = hog_img.astype("uint8")
    cv2.imshow("HOG Image", hog_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows