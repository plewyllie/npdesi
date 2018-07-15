import requests
requests.packages.urllib3.disable_warnings()

url = "https://apic/api/aaaLogin.json"

payload = "{\"aaaUser\":{\"attributes\":{\"name\":\"admin\",\"pwd\":\"cisco123\"}}}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "91b8b646-6a08-d6f0-41fb-8cdf4c245579"
    }

response = requests.request("POST", url, data=payload, verify=False, headers=headers)



print(response.text)

url = "https://apic/api/node/mo/uni/tn-Shipping.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-Shipping\",\"name\":\"Shipping\",\"rn\":\"tn-Shipping\",\"status\":\"created\"},\"children\":[]}}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "78f158b1-451f-cbac-86eb-bd8e104ddd6a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


