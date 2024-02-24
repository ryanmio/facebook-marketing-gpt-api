import json
import requests

def search_facebook_marketing(request):
    # Ensure the request is JSON
    request_json = request.get_json(silent=True)

    if request_json and 'terms' in request_json:
        search_terms = request_json['terms']
        data = []  # List to store results

        interests = [term.strip() for term in search_terms.split(',')]

        for interest in interests:
            url = f'https://graph.facebook.com/v16.0/search?type=adinterest&q={interest}&access_token=Your_Facebook_API_Access_Token'
            response = requests.get(url)
            
            if response.status_code == 200:
                json_response = response.json()

                for item in json_response.get('data', []):
                    data.append({
                        'name': item.get('name'),
                        'audience_size_lower_bound': item.get('audience_size_lower_bound'),
                        'audience_size_upper_bound': item.get('audience_size_upper_bound'),
                        'path': ' > '.join(item.get('path', [])),
                        'description': item.get('description', ''),
                        'topic': item.get('topic', '')
                    })
        return (json.dumps(data), 200, {'Content-Type': 'application/json'})
    else:
        return ('Invalid request: No search terms provided', 400)