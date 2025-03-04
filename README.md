# SlackAlertMailAgent_Langchain

## Overview
This project is an AI-driven workflow that automates email generation and sending based on error messages retrieved from Slack. It integrates multiple APIs to streamline communication and notification processes by interpreting these messages and generating meaningful email reports.

## Features
- Fetches recipient details from Google Sheets API.
- Retrieves error messages from Slack API.
- Uses AI to interpret and generate meaningful email content.
- Sends emails to designated recipients automatically.

## Technologies Used
- **LangChain** – AI-powered text interpretation and generation.
- **Slack API** – Retrieves error messages.
- **Google Sheets API** – Fetches recipient data.



## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mferen/SlackAlertMailAgent_Langchain.git
    ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables (Slack and OpenAI API keys, Google credentials).
4. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```


