import requests
import json
data = {
   "api_key": "PRIVATE_API_KEY",
   "profiles": [
       {
           "phone_number": "PHONE_NUMBER",
           "sms_consent": True
       }
   ]
}
headers = {
   "Content-Type": "application/json",
   "Cache-Control": "no-cache"
   }
conv = json.dumps(data)
response = requests.request("POST", "https://a.klaviyo.com/api/v2/list/LIST_ID/subscribe", data=conv, headers=headers)
print(response.text)
