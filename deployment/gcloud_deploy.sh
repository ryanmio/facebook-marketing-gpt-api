#!/bin/bash

# This script is now only used for manual deployments without token updates
gcloud functions deploy facebook_marketing_search \
  --runtime python39 \
  --trigger-http \
  --project=facebook-marketing-gpt-api \
  --allow-unauthenticated \
  --entry-point=search_facebook_marketing \
  --source=./src

gcloud functions deploy heartbeat_check \
  --runtime python39 \
  --trigger-http \
  --project=facebook-marketing-gpt-api \
  --entry-point=heartbeat_check \
  --source=./src