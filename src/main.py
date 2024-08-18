import json
import requests
import os
from heartbeat_check import heartbeat_check

def search_facebook_marketing(request):
    print("Function triggered, processing request...")  # Log when the function starts processing

    # Ensure the request is JSON
    request_json = request.get_json(silent=True)
    if not request_json or 'terms' not in request_json:
        print("Invalid or missing JSON payload in request.")
        return ('Invalid request: No search terms provided', 400)

    print(f"Received request JSON: {request_json}")  # Log the received JSON
    search_terms = request_json['terms']
    print(f"Search terms: {search_terms}")  # Log the search terms

    data = []  # List to store results
    interests = [term.strip() for term in search_terms.split(',')]
    access_token = os.environ.get('FACEBOOK_API_ACCESS_TOKEN', 'Your_Default_Access_Token_If_Not_Set')

    for interest in interests:
        print(f"Processing interest: {interest}")  # Log each interest being processed
        url = f'https://graph.facebook.com/v19.0/search?type=adinterest&q={interest}&access_token={access_token}'
        print(f"Requesting URL: {url}")  # Log the exact API request URL
        response = requests.get(url)
        
        if response.status_code == 200:
            json_response = response.json()
            print(f"API response for {interest}: {json_response}")  # Log the API response

            for item in json_response.get('data', []):
                data.append({
                    'name': item.get('name'),
                    'audience_size_lower_bound': item.get('audience_size_lower_bound'),
                    'audience_size_upper_bound': item.get('audience_size_upper_bound'),
                    'path': ' > '.join(item.get('path', [])),
                    'description': item.get('description', ''),
                    'topic': item.get('topic', '')
                })
        else:
            print(f"Failed to fetch data for {interest}. HTTP status code: {response.status_code}, Response: {response.text}")  # Log if the request failed

    print("Successfully processed request.")
    return (json.dumps(data), 200, {'Content-Type': 'application/json'})
