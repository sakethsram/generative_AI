import requests
import json
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDNtSlYp2vWFfqLnJpbDTwbqrkcvjO5yC8"
payload = json.dumps({
  "contents": [
    {
      "parts": [
        {
          "text": "list past prime ministers of  india"
        }
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
