from unittest.mock import DEFAULT

import requests
import json
import config
import asyncio



headers = {"X-Key": f"Key {config.API_KEY}",
           "X-Secret" : F"Secret {config.SECRET_KEY}",
}

URL = "https://api-key.fusionbrain.ai/"


async def generate( prompt,style="DEFAULT",images=1, width="1024", height='1024'):
    params = {
        "style":style,
        "type": "GENERATE",
        "numImages": images,
        "width": width,
        "height": height,
        "generateParams": {
            "query": f"{prompt}"
        }
    }

    files = {
        'model_id': (None,4),
        'params': (None, json.dumps(params), 'application/json')
    }
    response = requests.post(URL + "key/api/v1/text2image/run" , headers=headers,files=files)
    data = response.json()
    attempts = 0
    while attempts < 40:
        response = requests.get(URL + 'key/api/v1/text2image/status/' + data["uuid"], headers=headers)
        data = response.json()
        if data['status'] == 'DONE':
            return data['images']

        attempts -= 1
        await asyncio.sleep(3)