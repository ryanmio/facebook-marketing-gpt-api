#!/bin/bash

gcloud functions deploy facebook_marketing_search --runtime python39 --trigger-http --project=facebook-marketing-gpt-api --allow-unauthenticated --entry-point=search_facebook_marketing
