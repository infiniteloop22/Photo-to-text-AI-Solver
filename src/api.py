import requests
#import time
import json

class API:
    #def __init__(self):
        #pass
    @staticmethod
    def query_gpt4(api_key, question):
        response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions", 
        headers={
          "Authorization": f"Bearer {api_key}",
          "Content-Type": "application/json"
        },
        data=json.dumps({
          "model": "openai/gpt-oss-20b:free",
            "messages": [
              {
                "role": "user",
                "content": question
              }
            ],
          })
        )

        return response