# SMS Delivery Survey

Send an SMS survey once a product has been delivered to a client. Clients can rate the delivery experience: low ratings would trigger a follow-up survey to ask how to improve the delivery experience, high ratings would send a thank you message.

## Tools:
- [Klaviyo API](https://developers.klaviyo.com/en/reference/api-overview)
- [Python](https://www.python.org/)

## Instructions:

### 1. Create a Klaviyo Account
* For instructions: [Create a sandbox account.](https://developers.klaviyo.com/en/docs/create-a-test-account)

### 2. Generate sample data (dummy users)
* For instructions: [Generate sample data.](https://developers.klaviyo.com/en/docs/generate-sample-data)

### 3. Get your Public & Private API Keys
* For instructions: [Obtain API credentials.](https://developers.klaviyo.com/en/docs/retrieve-api-credentials)

### 4. Set up SMS
* For instructions: [How to turn on SMS in Klaviyo.](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)
* More information on the US/CA Toll-free number: [Understand toll-free number verification.](https://help.klaviyo.com/hc/en-us/articles/4415873897499-Understand-toll-free-number-verification)

### 5. Create your first Flow
The goal of this Flow is to receive feedback on the delivery experience once a user has received a product. 

#### 5.1 Set up the Flow
* Select "Flows" from the left menu.
* Click "Create Flow".
* Use a pre-built Flow, or in this case, click on "Create From Scratch".
* Give your Flow a name and tags (optional).
* For general instructions: [Getting started with flows.](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows)

#### 5.2 Customize the Flow
* We want the Metric "Fulfilled Order" to trigger the Flow:
  * Select "Metric", "Fulfilled Order", and press "Done".
* We want to send an SMS to the user once the order has been fulfilled:
  * Drag and drop the Action "SMS" on the node under the trigger "When someone Fulfilled Order".
  * Click on SMS #1 and edit it by clicking on the three dots.
  * Write the body of the SMS and add dynamic Properties as needed, e.g First Name. 
    * We want to invite the user to rate their delivery experience from 1 (low) to 5 (high).
    * Once you are done configuring your SMS, click "Save Content" and "Done".
* Now that the first SMS is set up, we want to create a Conditional Split based on the answer from the user: If the user rates the delivery between 1-4, we send them a follow-up survey; if the user rates the delivery 5, we send them a thank you message.
  * Drag and drop the Logic "Conditional Split" on the node below SMS #1 .
  * Configure your Conditional Split based on the SMS sent by the user:
    *  "Select a condition" > "What someone has done (or not done)" > "Choose Metric" > "Sent SMS".
  *  Then, add a Property to the Conditional Split:
     *  Funnel icon > "Choose property" > "Message Body" > "equals" > "1" > "at least once" > "since starting this flow".
  *  Repeat by clicking on the operator "AND" so that the "Message Body" equals 2, 3, and 4.
   * ![and](https://user-images.githubusercontent.com/48727972/189691600-6b66160b-2c66-4b9d-bdfc-1cd7d26b6017.png)

* Now that the Conditional Split is set up, we have two branches, Yes and No, which correspond to Conditional Split is True, or Conditional Split is False.
  * Set up an SMS under "YES" so that a follow up survey is sent to the user.
  * Set up an SMS under "NO" so that a thank you message is sent to the user.

#### 5.3 Analyze your Flow
* Click on "Show Analytics" from the top header.
* For more information: [Understanding flow analytics.](https://help.klaviyo.com/hc/en-us/articles/115002779351-Understanding-flow-analytics)
  * ![Flow](https://user-images.githubusercontent.com/48727972/189538053-99ad77a8-bb80-481f-88fe-8b2d1d62f91b.png)

### 6. Test your Flow with Klaviyo API

To test that your flow is functional, we are going to create a script in Python and use the Klaviyo API. 
* No need to create a new website, simply open your favorite web-based IDE (integrated development environment). For this project, I used [Replit](https://replit.com/).

#### 6.1 Add a new user and trigger the "Fulfilled Order" Metric
* Open [Replit.](https://replit.com/)
* Click "Create" and choose Python as your language.
* Copy/paste the script below and replace the private and public tokens with your own Public and Private Keys (see Step #3).
* Click on the Run button to run your script. You will see a light brown arrow under "Console" if you script was successfully launched.

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

* Explanation of the script:
  * We create a new user who has just fulfilled on order.
  * We add a phone number to the user's profile (customer_properties) to make sure they can receive the SMS from the Flow. 
* Pro Tips:
   * Remember that in Klaviyo, a user ID is defined by their email address. Make sure to add a new email address when creating a new user.
   * If you create a user with a US/CA phone number, make sure that your Toll-free number has already been verified (See Step #4) or that you subscribed to Klaviyo's Paid plan.

#### 6.2  Confirm that the new user was created in Klaviyo and that the Metric "Fulfilled Order" was added to their profile
* Go back to your Klaviyo dashboard.
* Click on "Profiles" under "Audience".
* If the script was run successfully, you will see the new user at the top of the list.
* Click on their name. Confirm that the metric "Fulfilled Order" is under Metrics. You should see a green (+1) next to this metric. 
  * ![fulfilled](https://user-images.githubusercontent.com/48727972/189691958-cfe25ddd-4b1c-4210-a6a1-ee8dc7b9f72f.png)

#### 6.3 Confirm that the Flow was triggered and that the first SMS was sent!
* Go back to your Klaviyo dashboard.
* Click on "Flows" and open the SMS Delivery Flow.
* Click on SMS #1 to check the associated analytics.
  * If you see a 1 next to Delivered, the SMS was successfully sent!
  * If you see a 1 next to Skipped or Waiting instead, the SMS was not sent. 
    * For more information: [Most common reason an SMS is not delivered.](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message)
   * ![analytics](https://user-images.githubusercontent.com/48727972/189692527-2e6529d0-56d2-4e6d-ad67-5cfab790e3eb.png)

### 7. Where to go from there? Roadblocks and lessons

#### 7.1 US SMS
* My first roadblock was the impossibility to test the Flow with my phone number, as the Toll-Free number is still pending verification and there is no free option to send SMS to a US phone number.
  * Troubleshooting:
    * I created a free UK number and assigned it to a dummy user. I confirmed that the Flow was successfully triggered and that the first SMS was sent to the user, with a "waiting" status: the free UK number is limited and doesn't offer the option to reply to the SMS or consent to Klaviyo SMS. 
    * I followed [this documentation](https://help.klaviyo.com/hc/en-us/articles/360054803711#setup-requirements1) to implement SMS consent via API, but I was still unable to reply to the SMS. 
    * I duplicated my Flow so that the survey would be sent via email instead of SMS. I was not able to find a way to listen to the reply of the user (e.g. Sent Email), the way I previously did with my initial Flow (e.g. Sent SMS). 

#### 7.2 Open-ended survey
* My survey asks the user to rate their delivery experience from 1 to 5.
  * Issues:
    * What if the user answers the survey with additional text (e.g "Amazing, 5 stars!")?
    * What if the user answers by spelling the rating instead of using a numerical value (e.g "four")?
  * Possible solutions:
    * Send a link to the survey instead of asking the user to rate directly via SMS.
    * Create an interactive SMS Campaign with buttons for 1-5 (coding needed).
    * Create another Conditional Split that informs the user that their answer is invalid if they do not reply with 1-5 (e.g. "invalid answer").

#### 7.3 Lack of data
* Because I was not able to fully test the Flow, I was not able to collect data from the survey.
   * Once I get the data, what are the next steps? How do I want to collect, organize, filter and present the data?
     * Create a new segment for users who rated the delivery experience.
     * Create a new segment for users who rated the delivery experience AND completed the survey.
     * Extract the data from the ratings & surveys with the Klaviyo API and/or CSV export.

#### 7.4 What are some questions I wish I could have answered with this Project? 
* Which **products** have on average the lowest or highest delivery experience rate? Why?
* Which **countries** have on average the lowest or highest delivery experience rate? Why?
* Is their a **time of the year** when users have a lower delivery experience? 
   * Delays? Do businessed need to communicate with their users beforehand if delays are expected (weather, holiday season), to manage expectations? 
* What else could we learn from these ratings and surveys?
