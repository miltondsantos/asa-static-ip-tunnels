#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ASA Static IP Tunnels Console Script.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Drew Taylor"
__email__ = "dretaylo@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from static_tunnels import *

if __name__ == "__main__":
    users = []
    START_IP = '10.0.0.1'
    DEVICE = 'vpn-hostname'
    AAA_SERVER = 'AAA_Server'
    GROUP_POLICY = "Default_Group_Policy"

    with open('./users.txt') as f:
        users = f.read().split()

    output = generateStaticTunnelsConfig(users, DEVICE, START_IP, AAA_SERVER, GROUP_POLICY)

    with open('./output/config.txt', 'w') as f:
        f.write(output)

    clear_output = clearStaticTunnelsConfig(users)

    with open('./output/clear_config.txt', 'w') as f:
        f.write(clear_output)