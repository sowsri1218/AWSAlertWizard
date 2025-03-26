# AWSAlertWizard


AWSAlertWizard is a serverless pipeline designed to fetch weather data from an open-source API (like Open-Meteo), analyze it for bad weather conditions, and send real-time alerts to email addresses using Amazon SES. and it also stores historical weather data in DynamoDB for future analysis.

## Features
- Fetches daily weather data using Open-Meteo API.
- Stores weather data in AWS DynamoDB for easy querying and persistence.
- Detects predefined "bad weather" conditions (e.g., heavy rainfall or extreme temperatures).
- Sends email alerts via Amazon Simple Email Service (SES).
- Fully automated pipeline with AWS Lambda and CloudWatch Event Rule.

## Prerequisites
1. **AWS Account**: Access to AWS services like Lambda, DynamoDB, and SES.
2. **Python**: Installed on your local machine for packaging the Lambda function.
3. **Install Required Libraries**:
   - Use `pip install requests -t .` to package the requests library for Lambda.
4. **IAM Role**: Identity and Access Management role is important for granting permission to AWS lambda function       to interact securely with other AWS services.


## Setup Guide

### 1. Create a DynamoDB Table
- Navigate to the DynamoDB Console and create a table:
  - **Table Name**: `WeatherData`
  - **Primary Key**: `Date` (String)

### 2. Set Up IAM Role
- In the IAM Console, create a role with the following policies:
  - **AWSLambdaBasicExecutionRole** for Lambda logging.
  - **AmazonDynamoDBFullAccess** for database access.
  - **AmazonSESFullAccess** for email notifications.
- Attach the role to the Lambda function.

### 3. Create Lambda Function
- Navigate to the AWS Lambda Console.
- Author a function named `WeatherDataHandler` and upload the zipped code package containing:
  - `requests` library dependencies.
  - Python script (`lambda_function.py`) for fetching weather data and storing it in DynamoDB.

### 4. Verify Email Address in SES
- Go to the SES Console and verify the sender and receiver email addresses under **Verified Identities**.

### 5. Automate with CloudWatch EventRule
- Create a scheduled rule in CloudWatch to trigger the Lambda function at specified intervals.
  
## Usage

**1. Clone the repository:**
   
   git clone https://github.com/sowsri1218/AWSAlertWizard.git
   cd AWSAlertWizard

**2. Package and Deploy:**

   Create a lambda_package directory, install dependencies(requests), and zip the files.

   Upload the zipped package to AWS Lambda.

**3. Test the Setup:**

   Trigger the Lambda function manually or let the scheduled rule execute it.

 **4.Monitor Alerts:**

   Check the verified email for weather alert notifications.
