import klaviyo

client = klaviyo.Klaviyo(public_token='PUBLIC_KEY')
private_token='PRIVATE_API_KEY'

def sendToKlaviyo():
  client.Public.track(
    'Fulfilled Order',
    email='test@gmail.com',
#     customer_properties={
#       "$first_name":"FIRST_NAME",
#       "phone_number":"PHONE_NUMBER",
#       "$city":"CITY, STATE",
#     }, 
  )
sendToKlaviyo()
