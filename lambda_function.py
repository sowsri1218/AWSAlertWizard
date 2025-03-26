import boto3
import json
import requests

# Initialize SES and DynamoDB clients
ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WeatherData')

def send_email_alert(subject, message):
    """
    Sends an email alert using Amazon SES.
    """
    ses.send_email(
        Source='sowjanyathumma@gmail.com',  # Replace with your verified email
        Destination={
            'ToAddresses': ['sowjanyathumma@gmail.com']  # Replace with the recipient's email
        },
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': message}}
        }
    )

def lambda_handler(event, context):
    """
    Fetch weather data, store it in DynamoDB, and send an alert if bad weather is detected.
    """
    # Fetch weather data from Open-Meteo API
    latitude = 49.25  # Example for Burnaby, BC
    longitude = -123.12
    url = f'https://api.open-meteo.com/v1/forecast?latitude=49.25&longitude=-123.12&daily=temperature_2m_max,precipitation_sum&timezone=auto'


    response = requests.get(url)
    if response.status_code != 200:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to fetch weather data.')
        }

    weather_data = response.json()
    daily_data = weather_data['daily']
    dates = daily_data['time']
    temps = daily_data['temperature_2m_max']
    precipitation = daily_data['precipitation_sum']

    # Process weather data
    for i in range(len(dates)):
        date = dates[i]
        temp = temps[i]
        rain = precipitation[i]

        # Store data in DynamoDB
        table.put_item(
            Item={
                'Date': date,
                'TemperatureMax': str(temp),
                'PrecipitationSum': str(rain)
            }
        )

        # Check for bad weather (example: precipitation > 50mm)
        if temp < 20:  # Example threshold for cold weather
            send_email_alert(
                "Bad Weather Alert!",
                f"Low temperature detected in Vancouver: {temp}°C."
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Weather data processed and stored successfully!')
    }
