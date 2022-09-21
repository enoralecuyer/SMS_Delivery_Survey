import requests

url = "https://a.klaviyo.com/api/v2/list/LIST_ID/members?api_key=PRIVATE_API_KEY"

payload = {"profiles": {"phone_number": "+11231123123", "email":"test@gmail.com"}}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

print(response.text)
