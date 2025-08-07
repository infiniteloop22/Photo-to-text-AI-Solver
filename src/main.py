from ocr import OCR
from display import Display
#import numpy as np
#import os

def main():
    #Display.frame_capture()
    img = Display.preprocess_img()
    OCR.perform_OCR(img)

    #adaptive_image = "test_images/img_adpt_thrs.png"
    #blurred_image = "test_images/img_blur.png"
    #grayscale_image = "test_images/img_grayscale.png"
    #perform_OCR(adaptive_image)
    #perform_OCR(blurred_image)
    #perform_OCR(grayscale_image)
    #png = "test_images/unnamed.png"
    #perform_OCR(png)

if __name__ == "__main__":
    main()