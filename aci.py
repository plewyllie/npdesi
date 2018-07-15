import requests
requests.packages.urllib3.disable_warnings()

url = "https://apic/api/aaaLogin.json"

payload = "{\"aaaUser\":{\"attributes\":{\"name\":\"admin\",\"pwd\":\"cisco123\"}}}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, verify=False, headers=headers)

print(response.text)

cookie = response.cookies

url = "https://apic/api/node/mo/uni/tn-Procurement.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-Procurement\",\"name\":\"Procurement\",\"rn\":\"tn-Procurement\",\"status\":\"created\"},\"children\":[]}}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, cookie=cookie, verify=False, headers=headers)

print(response.text)
