#!/usr/bin/env python3
import re

gui_config_first_part = """
{
  "version": "1.2.3.4",
  "configs": [
"""

gui_config_second_part = """
  ],
  "strategy": null,
  "index": 6,
  "global": true,
  "enabled": false,
  "shareOverLan": true,
  "isDefault": false,
  "isIPv6Enabled": false,
  "localPort": 10800,
  "portableMode": true,
  "pacUrl": null,
  "useOnlinePac": false,
  "secureLocalPac": true,
  "availabilityStatistics": true,
  "autoCheckUpdate": true,
  "checkPreRelease": false,
  "isVerboseLogging": true,
  "logViewer": {
    "topMost": false,
    "wrapText": false,
    "toolbarShown": false,
    "Font": "Consolas, 8pt",
    "BackgroundColor": "Black",
    "TextColor": "White"
  },
  "proxy": {
    "useProxy": false,
    "proxyType": 0,
    "proxyServer": "",
    "proxyPort": 0,
    "proxyTimeout": 3,
    "useAuth": false,
    "authUser": "",
    "authPwd": ""
  },
  "hotkey": {
    "SwitchSystemProxy": "",
    "SwitchSystemProxyMode": "",
    "SwitchAllowLan": "",
    "ShowLogs": "",
    "ServerMoveUp": "",
    "ServerMoveDown": "",
    "RegHotkeysAtStartup": false
  }
}
"""

def generate(port, passwd, list_of_host_method_pair):
    with open("out/gui-config.json", "w") as f:
        f.write(gui_config_first_part)
        for host_method_pair in list_of_host_method_pair:
            f.write("""
            {{
              "server": "{svr}",
              "server_port": {port},
              "password": "{password}",
              "method": "{encryption}",
              "plugin": "",
              "plugin_opts": "",
              "plugin_args": "",
              "remarks": "",
              "timeout": 5
            }},
            """.format(svr=host_method_pair[0], encryption=host_method_pair[1], port=port, password=passwd)
            )
        f.write(gui_config_second_part)