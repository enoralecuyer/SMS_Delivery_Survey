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

### 4. Set up SMS
* For instructions: [How to turn on SMS in Klaviyo ](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)
* More information on the US/CA Toll-free number: [Understand toll-free number verification ](https://help.klaviyo.com/hc/en-us/articles/4415873897499-Understand-toll-free-number-verification)

### 5. Create your first Flow
The goal of this Flow is to receive feedback on the delivery experience, once a user has received a Product. 

#### 5.1. Set up the Flow
* Select "Flows" from the left menu
* Click "Create Flow"
* Use a pre-built Flow, or in this case, click on "Create From Scratch"
* Give your flow a name and tags (optional)

#### 5.2. Customize the Flow
* Select "Metric" to trigger the flow when a user takes a specific action, in this case "Fulfilled Order", and press "Done"
* We want to send an SMS to the user once the order has been fulfilled:
  * Under "Actions", drag and drop "SMS" under the trigger "When someone Fulfilled Order"
  * Click on SMS #1, click on the three dots and "Edit". 
  * Write the body of your SMS and add dynamic Properties as needed, e.g First Name. 
    * Invite the user to rate their delivery experience from 1 (low) to 5 (high).
  * Once you are done configuring your SMS, click "Save Content" and "Done".
* Now that we have the content of the SMS, we need to create a Conditional based on the answer from the user: If the user rates the delivery between 1-3, we send them a follow-up survey to gather more data; if the user rates the delivery between 4-5, we send them a thank you SMS. 
 * Under "Logic", drag and drop "Conditional Split" below SMS #1 
 * Configure your Conditional Split:
   *  Click on the drop-down menu "Select a condition" > What someone has done (or not done) > Choose Metric > Sent SMS
   *  Then, add a property by clicking on the funnel icon > Choose property > Message Body > Equals > 1 > at least once > since starting this flow
   *  Click "AND" and repeat for Message Body equals 2 and 3, and Save
   * ![conditional](https://user-images.githubusercontent.com/48727972/189550497-54377d4f-5d7b-44df-b939-da0758092d65.png)

* If the user has replied in the body of the SMS 1, 2, or 3, the Conditional is True (Yes). They will then receive an SMS with a survey. Insert the SMS #2 under "YES"
* If the user has replied in the body of the SMS 4 or 5, the Conditioanl is False (No). They will receive a Thank you SMS. Insert the SMS #3 under "NO"

#### 5.3. Analyze your Flow
* Click on "Show Analytics" to display the rates of success of your Flow
  * ![Flow](https://user-images.githubusercontent.com/48727972/189538053-99ad77a8-bb80-481f-88fe-8b2d1d62f91b.png)

### 6. Test your Flow with Klaviyo API

To test that your flow is functional, we are going to create a script in Python and use the Klaviyo API. 
* No need to create a new website, simply open your favorite web-based IDE (integrated development environment). For this project, I used [Replit](https://replit.com/).

#### 6.1 Add a new user and trigger the "Fulfilled Order" metric
* Open [Replit](https://replit.com/)
* Choose Python as your language
* Import klaviyo and replace the private and public tokens with your own Public and Private Keys (see Step #3)
```python
import klaviyo

client = klaviyo.Klaviyo(public_token='******')
private_token='pk_**********************************'

def sendToKlaviyo():
  client.Public.track(
    'Fulfilled Order',
    email='enoratest@gmail.com',
    customer_properties={
      "$first_name":"Enora",
      "phone_number":"+1*********",
      "$city":"Aliso Viejo, CA",
    },
  )

sendToKlaviyo()
```

* Remember that in Klaviyo, a user's ID is defined by their email address. Make sure to add a new one when creating a new user
* Add as many customer_properties as needed
   * Note: The phone numbers of your test users in the US/CA, you will need to wait for your Toll-free number to be verified (see Step #4)
* Then, click on the Run button to run your script. You will see a light brown arrow under "Console" if you script was successfully launched
  * ![shell](https://user-images.githubusercontent.com/48727972/189552537-a691a15f-f3fa-48ad-b68c-7943f1fce475.png)

#### 6.2  Verify in Klaviyo that the new user was created and that the Metric "Fulfilled Order" was added to their profile
* Go back to your Klaviyo dashboard
* Click on "Profiles" under "Audience"
* If the script was run successfully, you will see the new user at the top of the list.
* Click on their name. Confirm that the metric "Fulfilled Order" is under Metrics. You should see a green (+1) next to this metric. 
![fulfilled](https://user-images.githubusercontent.com/48727972/189551499-e9737f63-6a2d-4fbd-b14b-1ef8a5f19f4e.png)

#### 6.3 Let's Analyze the Flow and confirm that the SMS was triggered!
* Go back to your Klaviyo dashboard
* Click on "Flows" and open the SMS Delivery Flow by clicking on its name
* Click on SMS #1 and view Analytics on the left-sided menu
 * If you see a 1 next to Delivered, the SMS was successfully sent!
 * If you see a 1 next to Skipped or Waiting instead, the SMS was not sent. 
   * For more information: [Most common reason an SMS is not delivered](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message)
   * ![analytics](https://user-images.githubusercontent.com/48727972/189551732-07b57bd3-bd29-45ee-89ae-b7bb7760ab0c.png)

### 7. Where to go from there? Roadblocks and lessons

#### 7.1 US SMS
* My first roadblock was the impossibility to test my Flow on my phone number, as the Toll-Free number is still pending verification and there is no free option to send SMS to a US user from a personal phone.  
  * To resolve, I created a free UK number and confirmed that the SMS #1 from the Flow was sent, but its Status is "Waiting" and I am unable to answer the SMS to give the delivery experience a rating. 
* My second roablock is that I was not able to validate the customer_properties={$consent: True}, to authorize a test user to receive a US SMS. 
  * To resolve, I tried to replicate my Flow with an email survey instead of a SMS survey to confirm that the email would be sent once the metric "Fulfilled Order" would be triggered. 
 * I was not able to find a way to listen to the metric "Sent Email" to listen to the rating of a test user, the way I configured it with "Sent SMS" on my primary SMS Flow. 

#### 7.2 Open-ended survey
* My survey ask the user to rate their delivery experience from 1 to 5. What if they answer with a spelled number instead of a numerical number (e.g. five instead of 5)? What if they add more text to the body of the SMS (e.g. excellent, 5 stars!)? 
* I was not sure if I wanted to send a survey for users who rated the experience 4 stars. Do we want to gather more data to see how the delivery experience could have been improved and become a 5?

#### 7.3 Lack of data
* Because I was not able to fully test the Flow, I was not able to collect the data from the survey.
 * Once I get the data, what is the next step? How do I want to collect, organize, filter and present the data? (ref: the 5 W)

#### 7.4 What are some questions I wish I could have answered with this Project? 
* Which products have on average the lowest delivery experience rate? Why?
* Which products have on average the highest delivery experience rate? Why?
* Which countries have on average the lowest delivery experience rate? Why?
* Which countries have on average the highest delivery experience rate? Why?
