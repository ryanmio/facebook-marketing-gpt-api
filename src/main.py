import json
import requests
from flask import escape

def search_facebook_marketing(request):
    # Ensure the request is JSON
    request_json = request.get_json(silent=True)

    # Check if the request JSON has 'terms' key
    if request_json and 'terms' in request_json:
        search_terms = request_json['terms']
        data = []  # List to store results

        # Split the search terms by comma and strip whitespace
        interests = [term.strip() for term in search_terms.split(',')]

        for interest in interests:
            # Construct the Facebook Marketing API URL
            url = f'https://graph.facebook.com/v16.0/search?type=adinterest&q={interest}&access_token=Your_Facebook_API_Access_Token'
            
            # Make the API request
            response = requests.get(url)
            
            # Check for a valid response before proceeding
            if response.status_code == 200:
                json_response = response.json()

                # Process each item in the response data
                for item in json_response.get('data', []):
                    data.append({
                        'name': item.get('name'),
                        'audience_size_lower_bound': item.get('audience_size_lower_bound'),
                        'audience_size_upper_bound': item.get('audience_size_upper_bound'),
                        'path': ' > '.join(item.get('path', [])),
                        'description': item.get('description', ''),
                        'topic': item.get('topic', '')
                    })

        # Return the compiled results as JSON
        return json.dumps(data), 200, {'Content-Type': 'application/json'}
    else:
        return 'Invalid request: No search terms provided', 400
