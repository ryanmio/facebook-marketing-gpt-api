# Facebook Token Exchange Tool

This tool helps you generate a long-lived access token for Facebook API access. This token is required for both the main marketing API function and the heartbeat check function.

## Getting a Long-Lived Token

1. Go to [Facebook Access Token Tool](https://developers.facebook.com/tools/accesstoken/)
2. Find your app in the list
3. Copy the "User Token" (this is your short-lived token)
4. Run the token exchange script:
   ```bash
   python3 src/exchange_token.py
   ```
5. Paste in your short-lived token when prompted
6. Copy the long-lived token that is generated

## Updating Your Functions

You'll need to update the token in two places:

### 1. Main Marketing API Function
Update the `FB_ACCESS_TOKEN` secret in your Google Cloud Function:
- Go to your function in Google Cloud Console
- Click "Edit"
- Scroll to "Runtime, build, connections and security settings"
- Expand "Security"
- Under "Runtime environment variables", find or add `FB_ACCESS_TOKEN`
- Paste your new long-lived token as the value
- Click "Deploy"

### 2. Heartbeat Check Function
Update the token in your heartbeat check function the same way:
- Go to your heartbeat check function in Google Cloud Console
- Follow the same steps as above to update the `FB_ACCESS_TOKEN`
- Click "Deploy"
