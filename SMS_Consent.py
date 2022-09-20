import requests
import json
data = {
   "api_key": "PRIVATE_KEY",
   "profiles": [
       {
           "phone_number": "PHONE NUMBER WITH COUNTRY CODE",
           "sms_consent": True
       }
   ]
}
headers = {
   "Content-Type": "application/json",
   "Cache-Control": "no-cache"
   }
conv = json.dumps(data)
response = requests.request("POST", "https://a.klaviyo.com/api/v2/list/LIST_CODE/subscribe", data=conv, headers=headers)
print(response.text)
