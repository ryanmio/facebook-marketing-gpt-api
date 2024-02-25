#!/bin/bash

export FACEBOOK_API_ACCESS_TOKEN='Your_Facebook_API_Access_Token'
gcloud functions deploy YOUR_FUNCTION_NAME --runtime python39 --trigger-http --set-env-vars FACEBOOK_API_ACCESS_TOKEN=Your_New_Token