# SMS Delivery Survey

Send an SMS survey once a product has been delivered to a client. Clients can rate the delivery experience: low ratings would trigger a follow-up survey to ask how to improve the delivery experience, high ratings would send a thank you message.

## Tools:
- [Klaviyo API](https://developers.klaviyo.com/en/reference/api-overview)
- [Python](https://www.python.org/)

## Instructions:

### 1. Create a Klaviyo Account
* For instructions: [Create a sandbox account](https://developers.klaviyo.com/en/docs/create-a-test-account)

### 2. Generate sample data (dummy users)
* For instructions: [Generate sample data](https://developers.klaviyo.com/en/docs/generate-sample-data)

### 3. Get your Public & Private API Keys
* For instructions: [Obtain API credentials](https://developers.klaviyo.com/en/docs/retrieve-api-credentials)

### 4 Set up SMS
* For instructions: [How to turn on SMS in Klaviyo ](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)
* More information on the US/CA Toll-free number: [Understand toll-free number verification ](https://help.klaviyo.com/hc/en-us/articles/4415873897499-Understand-toll-free-number-verification)

### 5. Create your first Flow
#### 3.1. Initial set up
* Select "Flows" from the left menu
* Click "Create Flow"
* Use a pre-built Flow, or in this case, click on "Create From Scratch"
* Give your flow a name and tags (optional)
#### 3.2 Create the Flow
* In this instance, we want to create a flow once a product has been delivered to a client, "Order Fulfilled"







**Flow from Klaviyo with integrated Analytics**
- ![Flow](https://user-images.githubusercontent.com/48727972/189538053-99ad77a8-bb80-481f-88fe-8b2d1d62f91b.png)

**Klaviyo API to create a new user and create the event 'Fulfilled Order'**
- ![Python](https://user-images.githubusercontent.com/48727972/189538238-e5dc5e4b-c9d9-418f-9598-9eadeaf76cc8.png)

**Waiting for the Toll-free US number to be verified** [(help center article)](https://help.klaviyo.com/hc/en-us/articles/4415873897499-Understand-toll-free-number-verification)
![verifying](https://user-images.githubusercontent.com/48727972/189538660-d4b92d67-a2d7-4e61-8080-4641a77bb795.png)

[Most common reason an SMS is not delivered](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message)
