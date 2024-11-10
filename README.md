# Facebook Marketing API Interest Finder

A powerful tool for discovering targetable interests on Facebook Ads using the Marketing API. This project includes both a cloud function for API searches and utilities for token management.

## Overview

This tool provides two main functionalities:
1. Search Facebook's Marketing API for targetable interests
2. Manage Facebook API access tokens

Unlike Facebook's in-platform tool which requires exact matches, this API-based approach searches across names, descriptions, and paths to find relevant interests for ad targeting.

## Features

### 1. Interest Search Function
- Searches across multiple terms simultaneously
- Returns detailed interest information:
  - Name
  - Audience size (upper and lower bounds)
  - Categorization path
  - Description
  - Topic
- Handles multiple search terms via comma-separated strings
- Returns results in JSON format

### 2. Token Management
- Exchanges short-lived tokens for long-lived tokens
- Automatically deploys new tokens to cloud functions
- Handles SSL certificate verification
- Includes manual deployment options

## Setup and Installation

### Token Setup
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

### Manual Deployment
If you need to deploy without updating tokens:
```bash
./deployment/gcloud_deploy.sh
```

## API Usage

### Endpoint
```
https://us-central1-facebook-marketing-gpt-api.cloudfunctions.net/facebook_marketing_search
```

### Request Format
```json
{
  "terms": "comma,separated,search,terms"
}
```

### Response Format
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

## Search Strategy

The tool follows a structured approach to find relevant interests:

1. **Audience Analysis**
   - Considers core interests and attributes
   - Analyzes lifestyle, values, and behaviors
   - Identifies relevant brands and activities

2. **Search Term Selection**
   - Uses precise, concise terms
   - Includes common variations
   - Avoids unnecessary qualifiers
   - Focuses on unique identifiers

3. **Result Filtering**
   - Validates relevance to target audience
   - Considers audience size ranges
   - Evaluates categorization paths


## Contributing

This project is maintained by Ryan Mioduski. For issues, feature requests, or contributions, please submit a pull request or open an issue in the repository.