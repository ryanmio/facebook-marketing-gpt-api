import requests
import os
import logging

def heartbeat_check(request):
    print("Heartbeat check triggered, processing...")

    access_token = os.environ.get('FACEBOOK_API_ACCESS_TOKEN', 'Your_Default_Access_Token_If_Not_Set')
    
    # Perform a simple API call to check if the token is valid
    url = f'https://graph.facebook.com/v19.0/search?type=adinterest&q=test&access_token={access_token}'
    response = requests.get(url)
    
    if response.status_code == 200:
        print("API key is valid.")
        return "API key is valid.", 200
    else:
        error_message = f"API key is invalid. Status code: {response.status_code}, Response: {response.text}"
        logging.error(error_message)
        return "API key is invalid. Error logged.", 500