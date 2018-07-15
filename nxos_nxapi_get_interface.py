#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface mgmt0",
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

    #print 'Status Code: ' + str(response.status_code)
    rx_object = json.loads(response.text)
    body_object = rx_object["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]
    #print json.dumps(rx_object, indent=4)
    print 'Management Interface Information' 
    print 'IP Address: {0}'.format(body_object["eth_ip_addr"])
    print 'Speed: {0}'.format(body_object["eth_speed"])
    print 'State: {0}'.format(body_object["state"])
    print 'MTU: {0}'.format(body_object["eth_mtu"])

    #print rx_object['ins_api']


