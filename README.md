# Facebook Marketing API Interest Finder

Backend service for Custom GPTs to search Facebook's Marketing API for ad targeting interests. Includes token management and cloud function deployment utilities.

## Overview

This service does two things:
1. Searches Facebook's Marketing API for targetable interests
2. Manages Facebook API access tokens

The API search checks names, descriptions, and paths - finding more interests than Facebook's in-platform tool which only does exact matches.

## Features

### 1. Interest Search Function
Returns:
- Interest name
- Audience size range
- Category path
- Description
- Topic

Takes comma-separated search terms, returns JSON.

### 2. Token Management
- Converts short-lived tokens to long-lived tokens
- Deploys tokens to cloud functions
- Handles SSL certificates
- Has manual deployment option

## Setup

### Token Setup
1. Go to [Facebook Access Token Tool](https://developers.facebook.com/tools/accesstoken/)
2. Find your app
3. Copy the User Token (short-lived token)
4. Run:
   ```bash
   python3 src/exchange_token.py
   ```
5. Paste your token when prompted
6. Type 'y' to deploy to both functions

The script will:
- Get your long-lived token
- Deploy it to both functions
- Show you the new token

### Manual Deploy
To deploy without updating tokens:
```bash
./deployment/gcloud_deploy.sh
```

## API Usage

### Endpoint
```
https://us-central1-facebook-marketing-gpt-api.cloudfunctions.net/facebook_marketing_search
```

### Request
```json
{
  "terms": "comma,separated,search,terms"
}
```

### Response
```json
[
  {
    "name": "Interest Name",
    "audience_size_lower_bound": 1000000,
    "audience_size_upper_bound": 1500000,
    "path": "Interests > Category > Subcategory",
    "description": "Interest description",
    "topic": "Topic category"
  }
]
```

## How It Searches

1. **Audience Analysis**
- Looks at core interests
- Checks behaviors and values
- Finds related brands/activities

2. **Search Terms**
- Uses short, specific terms
- Includes variations
- Skips unnecessary words
- Uses unique identifiers

3. **Results**
- Checks relevance
- Looks at audience size
- Reviews categories

## Contributing

Made by Ryan Mioduski. Open issues or PRs for changes.