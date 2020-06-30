import glob
import os
import copy
import shutil

SS_CONF_PATTERN = """
{{
   "server": "{ss_server}",
   "server_port": {ss_port},
   "local_address": "0.0.0.0",
   "local_port": {ss_local_port},
   "password": "{ss_passwd}",
   "timeout": 300,
   "method": "{ss_method}",
   "fast_open": false,
   "workers": 1
}}

"""

SS_SERVICE_PATTERN = """[Unit]
Description="SS-LOCAL"
Wants=network-online.target
After=network.target

[Timer]
OnBootSec=60

[Service]
Type=simple
ExecStart=/usr/local/bin/ss-local -c /etc/shadowsocks/{service_file}

[Install]
WantedBy=multi-user.target

"""

class ssconfig:
    def __init__(self, server, port, local_port, passwd, method):
        self.server = server
        self.port = port
        self.local_port = local_port
        self.passwd = passwd
        self.method = method

def name_it(ip_or_domain):
    return ip_or_domain.replace(".", "-")

def ss_generate(list_of_server_configs):
    jsons = []
    for config in list_of_server_configs:
        name = name_it(config.server) + ".json"
        jsons.append(name)
        with open("out/system/" + name, "w") as f:
            f.write(SS_CONF_PATTERN.format(
                ss_server=config.server,
                ss_port=config.port,
                ss_local_port=config.local_port,
                ss_passwd=config.passwd,
                ss_method=config.method
            )
            )
    workpath = os.getcwd()
    # find all ss service
    os.chdir("/etc/systemd/system/")
    services = copy.deepcopy(glob.glob("sss-*.service"))
    os.chdir(workpath)
    with open("out/system/ss_deploy.sh", "w") as f:
        for old_serv in services:
            f.write("systemctl stop {dotservice}\n".format(dotservice = old_serv))
            f.write("systemctl disable {dotservice}\n".format(dotservice = old_serv))
            
        for j in jsons:
            # .json
            f.write("cp {src} /etc/shadowsocks/{dst}\n".format(src=j, dst=j))
            # .service
            sf = "sss-{name}.service".format(name=j.replace(".json", ""))
            f.write("cp {src} /etc/systemd/system/{dst}\n".format(src=sf, dst=sf))
            f.write("systemctl enable {dotservice}\n".format(dotservice = sf))
            f.write("systemctl start {dotservice}\n".format(dotservice = sf))

            with open("out/system/" + sf, "w") as serf:
                serf.write(SS_SERVICE_PATTERN.format(service_file=j))





                    
