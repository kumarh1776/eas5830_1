import requests
import json

pinata_pin_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
pinata_gateway_url = "https://gateway.pinata.cloud/ipfs/"
api_key = "0d109a36711c233ec278"
api_secret = "20efb76ec43cab99b7ad24cd49dbb52e9e99251e4203d09db59a2ed1b4b0bcc5"

def pin_to_ipfs(data):
		assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
		json_data = json.dumps(data)

    headers = {
        'pinata_api_key': api_key,
        'pinata_secret_api_key': api_secret
    }

		files = {
        'file': ('data.json', json_data)
    }

		response = requests.post(f"{infura_url}/add", files = {"file": json_data})

		if response.status_code == 200:
				cid = response.json()["IpfsHash"]
				return cid
		else:
				raise Exception(response.text)

def get_from_ipfs(cid,content_type="json"):
		assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
    url = f"{pinata_gateway_url}{cid}"

		response = requests.get(url)
		
		if response.status_code == 200:
				if content_type == "json":
						data = response.json()
						assert isinstance(data,dict), f"get_from_ipfs should return a dict"
						return data
				else:
						raise Exception("Not dict")
		else:
				raise Exception(response.text)
