import requests
import json

def call_gemini_api():
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDNtSlYp2vWFfqLnJpbDTwbqrkcvjO5yC8"

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "input": "What’s the weather like today in Bangalore?" 
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    response_data = response.json()
    print("Response:", json.dumps(response_data, indent=2))

if __name__ == "__main__":
    call_gemini_api()
