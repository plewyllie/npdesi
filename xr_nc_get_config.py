#!/usr/bin/env python

from lxml import etree
from ncclient import manager

if __name__ == "__main__":

    with manager.connect(host='xrv', port=830, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'iosxr'},
                         allow_agent=False, look_for_keys=False) as device:


        nc_filter = """
            <config>
              <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
               <interface-configuration>
                <interface-name>Loopback100</interface-name>
               </interface-configuration>
              </interface-configurations>
            </config>
        """

        nc_reply = device.get(nc_filter)
        print nc_reply
