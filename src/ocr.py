import easyocr

class OCR:
    #def __init__(self):
        #passs
    @staticmethod
    def perform_OCR(img):
        reader = easyocr.Reader(['en'])
        #results = reader.readtext(img)

        results = reader.readtext(img, detail=0)  # detail=0 returns only text, not bounding boxes
        text = " ".join(results) if results else ""  # Join all detected text into a single string
        print(text)

        return text