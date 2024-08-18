#!/bin/bash

gcloud functions deploy facebook_marketing_search --runtime python39 --trigger-http --project=facebook-marketing-gpt-api --allow-unauthenticated --entry-point=search_facebook_marketing --source=./src

gcloud functions deploy heartbeat_check \
  --runtime python39 \
  --trigger-http \
  --project=facebook-marketing-gpt-api \
  --entry-point=heartbeat_check \
  --source=./src \
  --set-env-vars FACEBOOK_API_ACCESS_TOKEN=$FACEBOOK_API_ACCESS_TOKEN