# SMS Delivery Survey

Send an SMS survey once a product has been delivered to a client. Clients can rate the delivery experience: low ratings would trigger a follow-up survey to ask how to improve the delivery experience, high ratings would send a thank you message.

## Tools:
- [Klaviyo API](https://developers.klaviyo.com/en/reference/api-overview)
- [Python](https://www.python.org/)
- [Replit](https://replit.com/)

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
  *  Repeat by clicking on the operator "OR" so that the "Message Body" equals 2, 3, and 4.
   * ![and](https://user-images.githubusercontent.com/48727972/189691600-6b66160b-2c66-4b9d-bdfc-1cd7d26b6017.png)

* Now that the Conditional Split is set up, we have two branches, Yes and No, which correspond to Conditional Split is True, or Conditional Split is False.
  * Set up an SMS under "YES" so that a follow up survey is sent to the user.
  * Set up an SMS under "NO" so that a thank you message is sent to the user.
  
* Create the property Satisfied_With_Delivery (takes the values YES or NO) and add it to both branches of the Flow. Based on the rating of the delivery experience, the user will gain the property Satisfied_With_Delivery withe a value of NO or YES.
     * For more information: [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627-Profile-properties-reference)
  * ![no](https://user-images.githubusercontent.com/48727972/191355392-afcb063b-c6ad-4ca2-a7e8-9cef4fa938fd.png)

#### 5.3 Analyze your Flow
* Click on "Show Analytics" from the top header.
* For more information: [Understanding flow analytics.](https://help.klaviyo.com/hc/en-us/articles/115002779351-Understanding-flow-analytics)
  * ![Flow](https://user-images.githubusercontent.com/48727972/189538053-99ad77a8-bb80-481f-88fe-8b2d1d62f91b.png)

#### 5.4  Create two Segments based on the "Satisfied_With_Delivery" property
Create two Segments based on the "Satisfied_With_Delivery" property to automatically categorize users based on their delivery experience. 
    * For more information: [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments)

### 6. Secure SMS Consent from your users

#### 6.1 Send a SMS to your users and ask for their SMS consent
* To automatically send a SMS to your users and ask for their SMS consent, we are going to create a script in Python and use the Klaviyo API. 
  * No need to create a new website, simply open your favorite web-based IDE (integrated development environment). For this project, I used [Replit](https://replit.com/).
  * Open [Replit.](https://replit.com/)
  * Click "Create" and choose Python as your language.
  * Copy/paste the script below and replace the private with your own Public and Private Keys (see Step #3) as well of the ID of your List. 
  * Click on the Run button to run your script. You will see a light brown arrow under "Console" if your script was successfully launched. 
       * [Guide to Collecting SMS Consent via API](https://help.klaviyo.com/hc/en-us/articles/360054803711)
       * [How to find a list ID](https://help.klaviyo.com/hc/en-us/articles/115005078647-How-to-Find-a-List-ID)

``` python
import requests
import json
data = {
   "api_key": "pk_**********************************",
   "profiles": [
       {
           "phone_number": "+1**********",
           "sms_consent": True
       }
   ]
}
headers = {
   "Content-Type": "application/json",
   "Cache-Control": "no-cache"
   }
conv = json.dumps(data)
response = requests.request("POST", "https://a.klaviyo.com/api/v2/list/******/subscribe", data=conv, headers=headers)
print(response.text)
```
#### 6.2 Consent to SMS

* You will now receive an SMS asking you to consent to receiving SMS from Klaviyo. Type YES.
   * ![1](https://user-images.githubusercontent.com/48727972/191102212-56e6a432-caae-49f1-99f5-f3297446d980.jpg)

* Check the profile of your test user: you will see the new consent information under their phone number!
   * ![SMSConsent](https://user-images.githubusercontent.com/48727972/191351409-b197a7e7-4fdb-40b8-87b1-559f427db23b.png)

### 7. Test your Flow with Klaviyo API
To test that your flow is functional, we are going to create a script in Python and use the Klaviyo API. 
* No need to create a new website, simply open your favorite web-based IDE (integrated development environment). For this project, I used [Replit](https://replit.com/).

#### 7.1 Trigger the "Fulfilled Order" Metric
* Open [Replit.](https://replit.com/)
* Click "Create" and choose Python as your language.
* Copy/paste the script below and replace the private and public tokens with your own Public and Private Keys (see Step #3).
* Click on the Run button to run your script. You will see a light brown arrow under "Console" if your script was successfully launched.

```python
import klaviyo

client = klaviyo.Klaviyo(public_token='******')
private_token='pk_**********************************'

def sendToKlaviyo():
  client.Public.track(
    'Fulfilled Order',
    email='***********@gmail.com',
  )
sendToKlaviyo()
```

#### 7.2  Confirm that the Metric "Fulfilled Order" was added to the user's profile
* Go back to your Klaviyo dashboard.
* Click on "Profiles" under "Audience".
* If the script was run successfully, you will see the new user at the top of the list.
* Click on their name. Confirm that the metric "Fulfilled Order" is under Metrics. You should see a green (+1) next to this metric. 
  * ![fulfilled](https://user-images.githubusercontent.com/48727972/189691958-cfe25ddd-4b1c-4210-a6a1-ee8dc7b9f72f.png)

#### 7.3 Confirm that the Fulfilled Order Metric triggered the SMS #1 from our Flow
* Click on your user's name
* Under "Show All Metrics", you will see the most recent metrics associated with the user. 
![Screenshot 2022-09-20 at 12-57-45 Editing SMS_Delivery_Survey_README md at main · enoralecuyer_SMS_Delivery_Survey](https://user-images.githubusercontent.com/48727972/191353280-d78621cf-a66f-4a5c-b1c2-130e1d2746b0.jpg)

#### 7.3 Check the status of the SMS #1 from your Flow
Alternatively, you can also check directly from your Flow Analytics to confirm that the SMS #1 was sent or understand the reason why it was not sent
* Click on "Flows" and open the SMS Delivery Flow.
* Click on SMS #1 to check the associated analytics.
  * If you see a 1 next to Delivered, the SMS was successfully sent!
  * If you see a 1 next to Skipped or Waiting instead, the SMS was not sent. 
    * For more information: [Most common reason an SMS is not delivered.](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message)
   * ![analytics](https://user-images.githubusercontent.com/48727972/189692527-2e6529d0-56d2-4e6d-ad67-5cfab790e3eb.png)
   
#### 7.4 Give your delivery experience a rating and, if applicable, answer the survey
* ![20220919_154757](https://user-images.githubusercontent.com/48727972/191132895-a61118d7-6736-402d-95ca-5493a90cafd6.jpg)

### 8. Roadblocks

#### 8.1 US SMS
* My first roadblock was that I was waiting for the US Toll-Free number to be verified, and didn't realize that the reason why I was not receiving SMS was because I hadn't consented to SMS. 
  * Troubleshooting:
    * I created a free UK number and assigned it to a dummy user. I confirmed that the Flow was successfully triggered and that the first SMS was sent to the user, with a "waiting" status: the free UK number is limited and doesn't offer the option to reply to the SMS or consent to Klaviyo SMS. 
    * I duplicated my Flow so that the survey would be sent via email instead of SMS. I was not able to find a way to listen to the reply of the user (e.g. Sent Email), the way I previously did with my initial Flow (e.g. Sent SMS). 

#### 8.2 Unable to receive any SMS past my first test. 
* I realized that I had to remove Smart Sending and Quiet Hours o that users could receive several SMS in a row, at all hours of the day, which allowed me to continue my testing. 

#### 8.3 SMS #2 and #3 are sent in a row, without giving the user time to give a rating!
* The second conditional of my Flow would be sent automatically even before I had time to send my rating:
   * ![Screenshot_20220919-143954_Messages](https://user-images.githubusercontent.com/48727972/191125053-a52c8287-f249-47d3-a53e-036b690753a9.jpg)

* So I added a delay of 1 minute to give users some time to type their rating
  * ![delay1](https://user-images.githubusercontent.com/48727972/191125538-9a65a3b0-8c51-49f3-95df-32f3cd59e17d.png)

#### 8.4 "MESSAGE NOT RECEIVED" error message
* I was still receiving the message "MESSAGE NOT RECEIVED" when answering the survey.
   * Based on the SMS Settings, this error message is triggered when "no keyword is recognized"
* ![Screenshot_20220919-145057_Messages](https://user-images.githubusercontent.com/48727972/191126392-1b5a6df6-35ba-488a-99d7-76ae5064fb21.jpg)

* I updated the settings of the "MESSAGE NOT RECEIVED" to only be sent to users who have not consented to SMS, instead of sending it to every users who type a keyword that not recognized (not the ideal default setting). 
  * Before:
    * ![not received](https://user-images.githubusercontent.com/48727972/191128202-4536b321-845a-4b0c-bba3-6340bd224f93.png)
  * After:
    * ![update2](https://user-images.githubusercontent.com/48727972/191128265-87690490-49dc-4979-8247-829b42e3948a.png)

#### 8.51 Certain ratings (1-4) would not be recognized in my Flow
* I went back to my Flow to understand why some numbers (1-4) would not be recognized and I had a lightbulb moment: I created my conditional split with AND instead of OR. 
   * At that moment, only users who would text back 1234 would receive the survey, instead of users who would text back 1, 2, 3, or 4!!

#### 8.52 Keyword Management
* I tried to add some Compliance Keywords but realized that we couldn't add more of them, only update the existing ones. The Compliance Keyword "YES" was already taken, and I couldn't add numbers, so this was a dead end. 

#### 8.6 Testing different Flows
* ![conditional](https://user-images.githubusercontent.com/48727972/191130604-084fcd1b-fa06-449e-99fa-3b2170ba518c.png)
* ![split](https://user-images.githubusercontent.com/48727972/191132482-4d28243c-d6c6-43cc-8ff3-80e38f708d4f.png)

#### 8.7 Open-ended survey
* My survey asks the user to rate their delivery experience from 1 to 5.
  * Issues:
    * What if the user answers the survey with additional text (e.g "Amazing, 5 stars!")?
    * What if the user answers by spelling the rating instead of using a numerical value (e.g "four")?
  * Possible solutions:
    * Send a link to the survey instead of asking the user to rate directly via SMS.
    * Create an interactive SMS Campaign with buttons for 1-5 (coding needed).
    * Create another Conditional Split that informs the user that their answer is invalid if they do not reply with 1-5 (e.g. "invalid answer").

#### 8.8 Lack of data
* Because I was not able to fully test the Flow, I was not able to collect enough data from the survey.
   * How do I want to collect, organize, filter and present the data?
     * Create a new segment for users who rated the delivery experience.
     * Create a new segment for users who rated the delivery experience AND completed the survey.
     * Extract the data from the ratings & surveys with the Klaviyo API and/or CSV export.
     * How to extract the data from the SMS Conversations?
     * Send a refund or discount link to users who have rated the delivery experience poorly.

#### 8.9 404 Error on certain help center articles
* I tried to access the "Guide to SMS conversations in Klaviyo" from the article ["How to block, archive, or mark SMS conversations as unread"](https://help.klaviyo.com/hc/en-us/articles/4405329314331) but the link is broken. I did a manual search and was able to access the article. 
   * ![404](https://user-images.githubusercontent.com/48727972/191360105-22a8badb-5539-49d6-9bc9-bec269864f47.png)

### 9. Lessons and Food for Thoughts

#### 9.1 Lessons

I learned so much from this project!!
* I collaborated with Ingrid to understand how to trigger the SMS consent, how to define a condional split based on the body of the SMS, how to think in terms of metrics and not of lists to create dynamic processes!
* I learned how to use the Klaviyo API and Python to create new users, add new properties, trigger an event or an SMS...
* I learned to think strategically about the goal of my project, the architecture of my Flow, and the logical steps to get the user the exact answer they need
* I explored Klaviyo's Dashboard and Documentation quite thoroughly! 

#### 9.2 What are some questions I wish I could have answered with this Project? 
* Which **products** have on average the lowest or highest delivery experience rate? Why?
* Which **countries** have on average the lowest or highest delivery experience rate? Why?
* Is their a **time of the year** when users have a lower delivery experience? 
   * Delays? Do businessed need to communicate with their users beforehand if delays are expected (weather, holiday season), to manage expectations? 
