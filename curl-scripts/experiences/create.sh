#!/bin/bash

curl "http://localhost:8000/experiences/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "experience": {
      "what": "'"${WHAT}"'",
      "where": "'"${WHERE}"'",
      "notes": "'"${NOTES}"'"
    }
  }'

echo
