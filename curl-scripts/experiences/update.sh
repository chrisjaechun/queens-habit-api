#!/bin/bash

curl "http://localhost:8000/experiences/${ID}/" \
  --include \
  --request PATCH \
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
