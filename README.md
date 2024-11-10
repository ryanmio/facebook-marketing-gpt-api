# Facebook Token Exchange Tool

This tool helps you generate a long-lived access token for Facebook API access and automatically deploy it to your Google Cloud Functions.

## Getting a Long-Lived Token and Deploying

1. Go to [Facebook Access Token Tool](https://developers.facebook.com/tools/accesstoken/)
2. Find your app in the list
3. Copy the "User Token" (this is your short-lived token)
4. Run the token exchange script:
   ```bash
   python3 src/exchange_token.py
   ```
5. Paste in your short-lived token when prompted
6. When asked if you want to deploy, type 'y' to automatically update both functions

The script will:
- Exchange your short-lived token for a long-lived token
- Deploy the new token to both the main marketing API function and heartbeat check function
- Display the new token for your records

## Manual Deployment
If you need to deploy the functions without updating the token, use:
```bash
./deployment/gcloud_deploy.sh
```