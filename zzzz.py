import requests
import json
import config
import asyncio

from REQUEST import response

headers = {"X-KEY": f"KEY {config.API_KEY}",
           "X-Secret" : F"Secret {config.SECRET_KEY}",
}

URL = "https://api-key.fusionbrain.ai/"

async def generate(prompt):
	params = {
		"type": "GENERATE",
		"numImages": 1,
		"width": 1024,
		"height": 1024,
		"generateParams": {"query": prompt},
    }

    data = {
        'model_id': (None,4),
        'params': (None, json.dumps(params), 'application/json')
    }
    data = response.json()
    attempts = 0
    while attempts < 40:
        response = requests.get(URL + 'key/api/v1/text2image/status/' + data["uuid"], headers=headers)
        data = response.json()
        if data['status'] == 'DONE':
            return data['images']
        attempts += 1
        await asyncio.sleep(3)