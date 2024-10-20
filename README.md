# Spam Call Scammer Script

## Description

This script was created as a fun way to get back at scammers who send spam calls and texts. Using Twilio’s API, the script continuously makes automated calls to a specific phone number until manually stopped. It plays a pre-recorded message hosted on Twilio.

## Features

- Makes automated calls to a target number
- Plays a recorded message to the recipient
- Repeats calls every 15 seconds until you manually stop it
- Uses Twilio Functions to host the message

## Prerequisites 

- Python
- Twilio Account. You will need a paid version if you want to call unverified number
- Twilio Credentials. Account SID, Auth Token, and a Twilio phone number

# Installation

1. Clone the repo
```bash
    git clone https://github.com/carlosalonsovilla/scam-caller.git
    cd scam-caller
```
2. Install the required dependencies.
```bash
    pip install -r requirements.txt
```
3. Set up environment variables. Create a .env file in the project directory and add the following:
```
    ACCOUNT_SID=your_twilio_account_sid
    AUTH_TOKEN=your_twilio_auth_token
    TWILIO_NUMBER=your_twilio_phone_number
```

# Usage

1. Run the script
```bash
    python caller.py
```
2. The script will continuously make calls to the specified phone number, playing the pre-recorded message. You can stop the script by pressing Ctrl+C.
