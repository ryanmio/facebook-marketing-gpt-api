import urllib.request
import urllib.parse
import json
import ssl

def get_long_lived_token(app_id, app_secret, short_lived_token):
    """Exchange a short-lived token for a long-lived token."""
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': short_lived_token
    }
    
    url = f"https://graph.facebook.com/v12.0/oauth/access_token?{urllib.parse.urlencode(params)}"
    
    # Create SSL context that ignores certificate verification
    context = ssl._create_unverified_context()
    
    try:
        with urllib.request.urlopen(url, context=context) as response:
            data = json.loads(response.read().decode())
            return data.get('access_token')
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Hardcoded credentials
APP_ID = '1834532426990781'
APP_SECRET = '1d1616ad808a3fa682d7d2638ad36ac0'

# Get only the short-lived token from user
short_lived_token = input("Enter your short-lived token: ").strip()

# Get long-lived token
long_lived_token = get_long_lived_token(APP_ID, APP_SECRET, short_lived_token)

if long_lived_token:
    print("\nSuccessfully obtained long-lived token:")
    print(f"\n{long_lived_token}\n")
else:
    print("Failed to obtain long-lived token.") 