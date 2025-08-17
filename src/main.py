from ocr import OCR
from display import Display
from api import API
import json

def load_api_key() -> str:
    with open("config.json", 'r') as file:
        api_key = json.load(file)

    return api_key["API_KEY"]

def print_data(response):
    data = response.json()
    data_str = str(data)

    info = {"model" : data["model"], "message" : data["choices"][0]["message"]["content"]}

    if response.status_code == 200: # Successful http request
        print(f"Success! \nmodel: {info.get("model")} \nmessage: {info.get("message")}")
        with open("response data.txt", 'w') as file:
            file.write(data_str) # view contents
    else:
        print("Error: Could not retrieve data.")

def main():
    api_key = load_api_key()
    img = Display.frame_capture()
    #preprocessed_img = Display.preprocess_img(img)

    question = OCR.perform_OCR(img)
    response = API.query_gpt4(api_key, question)
    print_data(response)

if __name__ == "__main__":
    main()