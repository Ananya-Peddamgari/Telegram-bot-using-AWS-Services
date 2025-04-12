import requests

# Replace with your values
BOT_TOKEN = "your_api_token"
LAMBDA_URL = "invoke url of api gateway"

def set_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    data = {"url": LAMBDA_URL}
    
    try:
        # Set a reasonable timeout (in seconds)
        response = requests.post(url, data=data, timeout=30)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    set_webhook()
