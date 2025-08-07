import cv2 as cv
import sys

class Display:
    def __init__(self):
        pass

    def frame_capture():
        cap = cv.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Cannot open camera")
            exit()

        while True:
            # Capture the image frame-by-frame
            ret, frame = cap.read()

            # If frame is not read correctly
            if not ret:
                print("Error: Can't receive frame. Exiting...")
                break

            # Display the first frame
            cv.imshow('frame_color', frame)

            # Display the second frame
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)        
            cv.imshow('frame_gray', gray)

            key = cv.waitKey(1)

            if key == 32:
                cv.imwrite("captured_image_color.png", frame)
                cv.imwrite("captured_image_gray.png", gray)
                print("Frame(s) captured and saved as captured_image_xxx.png")
            elif key == 27:
                sys.exit("Exiting...")

        # Releasing the capture
        cap.release()
        cv.destroyAllWindows()

    def preprocess_img():
        #img_path = ".\\unnamed.png"
        #print(f"Checking image path: {os.path.abspath(img_path)}")

        while True:
            img1 = cv.imread("test_images/unnamed.png")
            img2 = cv.imread("test_images/unnamed.png", cv.IMREAD_GRAYSCALE)

            if img1 is None or img2 is None:
                sys.exit("Could not read specified image.")
    
            #cv.imshow("Original", img1)
            #cv.imshow("Grayscale Image", img2)

            # Operations on the image
            #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            blurred = cv.GaussianBlur(img2, (5, 5), 0)

            # Apply Adaptive Thresholding
            adaptive_thresh = cv.adaptiveThreshold(
            blurred, 255, 
            cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # Adaptive method
            cv.THRESH_BINARY,  # Convert to binary image
            11,  # Block size (size of neighborhood)
            2  # Constant subtracted from mean
            )
        
            #cv.imshow("Blurred image", blurred)
            cv.imshow("Adaptive threshold image", adaptive_thresh)

            key = cv.waitKey(1) # Waits for 1ms before checking key press

            if key == ord('s'):
                #cv.imwrite("test_images/img_grayscale.png", img2)
                #cv.imwrite("test_images/img_blur.png", blurred)
                cv.imwrite("test_images/img_adpt_thrs.png", adaptive_thresh)
                print("Saving image as img_xxx.png")
            elif key == 27:
                #sys.exit("Exiting...")
                print("Exiting...")
                return