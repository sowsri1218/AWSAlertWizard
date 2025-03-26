# AWSAlertWizard
# AWSAlertWizard

AWSAlertWizard is a serverless pipeline designed to fetch weather data from an open-source API (like Open-Meteo), analyze it for bad weather conditions, and send real-time alerts to email addresses using Amazon SES. The solution also stores historical weather data in DynamoDB for future analysis.

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


## Setup Guide

1. **Create a DynamoDB Table**:
   - Table Name: `WeatherData`
   - Primary Key: `Date` (String)

3. **Set Up AWS Lambda**:
   - Create a Lambda function in Python (`lambda_function.py`) to fetch weather data and save it to DynamoDB.

4. **Set Up Email Notifications**:
   - Verify your email with Amazon SES and configure the Lambda function to send alerts.

5. **Automate the Pipeline**:
   - Use AWS CloudWatch EventRule to schedule the Lambda function execution.

## Usage

**1. Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AWSAlertWizard.git
   cd AWSAlertWizard

**2. Package and Deploy:**

   Create a lambda_package directory, install dependencies(requests), and zip the files.

   Upload the zipped package to AWS Lambda.

**3. Test the Setup:**

   Trigger the Lambda function manually or let the scheduled rule execute it.

 **4.Monitor Alerts:**

   Check your verified email for weather alert notifications.
