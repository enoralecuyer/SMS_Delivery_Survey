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

#### 6. Test your Flow

To test that your flow is functional, we are going to create a script in Python and use the Klaviyo API. No need to create a new website, simply open your favorite web-based IDE (integrated development environment). In this case, I use [Replit](https://replit.com/).



**Klaviyo API to create a new user and create the event 'Fulfilled Order'**
- ![Python](https://user-images.githubusercontent.com/48727972/189538238-e5dc5e4b-c9d9-418f-9598-9eadeaf76cc8.png)

[Most common reason an SMS is not delivered](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Understanding-the-skipped-reason-for-a-flow-message)
