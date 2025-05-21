curl -i -X POST \
  --url https://chat-ai.academiccloud.de/v1/completions \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer <api_key>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "meta-llama-3.1-8b-instruct",
    "prompt": "hi there.",
    "max_tokens": 50,
    "temperature": 0.7
  }'

#
curl -i -X POST \
  --url https://chat-ai.academiccloud.de/v1/completions \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer <api_key>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "internvl2.5-8b",
    "prompt": "hi there.",
    "max_tokens": 50,
    "temperature": 0.7
  }'

#
curl -i -X POST \
  --url https://chat-ai.academiccloud.de/v1/completions \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer <api_key>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "gemma-3-27b-it",
    "prompt": "hi there.",
    "max_tokens": 50,
    "temperature": 0.7
  }'

#
curl -i -X POST \
  --url https://chat-ai.academiccloud.de/v1/completions \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer <api_key>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "qwen2.5-vl-72b-instruct",
    "prompt": "hi there.",
    "max_tokens": 50,
    "temperature": 0.7
  }'
