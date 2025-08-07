import easyocr

class OCR:
    def __init__(self):
        pass
    
    def perform_OCR(img):
        reader = easyocr.Reader(['en'])

        results = reader.readtext(img)

        if not results:
            print("No text found.")
            return

        print("\nOCR Results:")
        for bbox, text, confidence in results:
            print(f"Detected: '{text}' (Confidence: {confidence:.2f})")