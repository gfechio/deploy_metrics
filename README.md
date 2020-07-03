# Metrics for Deploy
Deploy api to calculate and manage how long does it takes to deploy new "things" to Production environment.

The API will receive:
* Component: What is been deployed
* Version: Version (self explained)
* Owner: The deploy Owner or Responsible ( at first  will be a person, robot TODO). Of course it needs a human to pull the strings
* Status: Deploy Status

What data will be persisted:
* Component: As above
* Version: As Above
* Onwer: As above
* Status: Start/Deploying/(DONE|ERROR)
* Date: Time and date of each request sent to the API with diofferent status, problably informing the Status above


# To Do

- Error creating Database
