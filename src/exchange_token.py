import urllib.request
import urllib.parse
import json
import ssl
import subprocess
import os

def get_long_lived_token(app_id, app_secret, short_lived_token):
    """Exchange a short-lived token for a long-lived token."""
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': short_lived_token
    }
    
    url = f"https://graph.facebook.com/v12.0/oauth/access_token?{urllib.parse.urlencode(params)}"
    context = ssl._create_unverified_context()
    
    try:
        with urllib.request.urlopen(url, context=context) as response:
            data = json.loads(response.read().decode())
            return data.get('access_token')
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def deploy_functions(token):
    """Deploy both functions with the new token."""
    print("\nDeploying functions with new token...")
    
    try:
        # Deploy main function
        subprocess.run([
            "gcloud", "functions", "deploy", "facebook_marketing_search",
            "--runtime", "python39",
            "--trigger-http",
            "--project=facebook-marketing-gpt-api",
            "--allow-unauthenticated",
            "--entry-point=search_facebook_marketing",
            "--source=./src",
            f"--set-env-vars=FACEBOOK_API_ACCESS_TOKEN={token}"
        ], check=True)
        
        # Deploy heartbeat function
        subprocess.run([
            "gcloud", "functions", "deploy", "heartbeat_check",
            "--runtime", "python39",
            "--trigger-http",
            "--project=facebook-marketing-gpt-api",
            "--entry-point=heartbeat_check",
            "--source=./src",
            f"--set-env-vars=FACEBOOK_API_ACCESS_TOKEN={token}"
        ], check=True)
        
        print("\nBoth functions successfully deployed with new token!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nError deploying functions: {str(e)}")
        return False

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
    
    # Ask user if they want to deploy
    deploy = input("Would you like to deploy the functions with this new token? (y/n): ").strip().lower()
    if deploy == 'y':
        deploy_functions(long_lived_token)
    else:
        print("\nToken generated but not deployed. You can deploy manually later.")
else:
    print("Failed to obtain long-lived token.") 