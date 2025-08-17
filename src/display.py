import cv2 as cv
import sys
import numpy as np

class Display:
    #def __init__(self):
        #pass
    @staticmethod
    def frame_capture():
        program = True
        cap = cv.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Cannot open camera")
            exit()

        while program:
            # Capture the image frame-by-frame
            ret, frame = cap.read()

            # If frame is not read correctly
            if not ret:
                print("Error: Can't receive frame. Exiting...")
                sys.exit()

            # Display the first frame
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame_color', gray)

            key = cv.waitKey(1)

            if key == 32: # space bar
                cv.imwrite("captured_image_color.png", gray)
                #cv.imwrite("captured_image_gray.png", gray)
                print("Frame captured and saved as captured_image_xxx.png")
                # Releasing the capture
                cap.release()
                cv.destroyAllWindows()
                return "captured_image_color.png"
            elif key == 27: # esc key
                program = False

    @staticmethod
    def preprocess_img(img):
        while True:
            # Operations on the image
            #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            blurred = cv.GaussianBlur(img, (5, 5), 0)
            blurred = np.uint8(blurred)

            # Apply Adaptive Thresholding
            adaptive_thresh = cv.adaptiveThreshold(
            blurred, 255, 
            cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # Adaptive method
            cv.THRESH_BINARY,  # Convert to binary image
            11,  # Block size (size of neighborhood)
            2  # Constant subtracted from mean
            )
        
            #cv.imshow("Blurred image", blurred)
            #cv.imshow("Adaptive threshold image", adaptive_thresh)

            #key = cv.waitKey(1) # Waits for 1ms before checking key press

            #if key == ord('s'):
                #cv.imwrite("test_images/img_grayscale.png", img2)
                #cv.imwrite("test_images/img_blur.png", blurred)
            preprocessed_img = cv.imwrite("test_images/img_adpt_thrs.png", adaptive_thresh)
            print("Saving image...")
            return preprocessed_img
            #elif key == 27: # esc key
                #return