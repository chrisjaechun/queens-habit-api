#!/bin/bash

curl "http://localhost:8000/experiences/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo