import requests

url = "https://apic/api/aaaLogin.json"

payload = "{\"aaaUser\":{\"attributes\":{\"name\":\"admin\",\"pwd\":\"cisco123\"}}}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "91b8b646-6a08-d6f0-41fb-8cdf4c245579"
    }

response = requests.request("POST", url, data=payload, verify='false', headers=headers)

print(response.text)
