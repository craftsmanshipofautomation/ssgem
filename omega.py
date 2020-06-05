import random

# todo: add auto switch

OMEGA_COMMON_TONGUE = """
    "-addConditionsToBottom": false,
    "-confirmDeletion": true,
    "-downloadInterval": 1440,
    "-enableQuickSwitch": false,
    "-monitorWebRequests": true,
    "-quickSwitchProfiles": [],
    "-refreshOnProfileChange": true,
    "-revertProxyChanges": true,
    "-showExternalProfile": true,
    "-showInspectMenu": true,
    "-startupProfileName": "",
    "schemaVersion": 2
"""

OMEGA_PROXY_PATTERN = """
    "+{node_name}": {{
        "bypassList": [
            {{
                "conditionType": "BypassCondition",
                "pattern": "127.0.0.1"
            }},
            {{
                "conditionType": "BypassCondition",
                "pattern": "::1"
            }},
            {{
                "conditionType": "BypassCondition",
                "pattern": "localhost"
            }}
        ],
        "color": "{node_color}",
        "fallbackProxy": {{
            "host": "127.0.0.1",
            "port": {node_port},
            "scheme": "socks5"
        }},
        "name": "{node_name}",
        "profileType": "FixedProfile",
        "revision": "{node_revision}"
    }},
"""
# for on windows, there is only one port
OMEGA_PROXY_PATTERN_FOR_WINDOWS = """
    "+{node_name}": {{
        "bypassList": [
            {{
                "conditionType": "BypassCondition",
                "pattern": "127.0.0.1"
            }},
            {{
                "conditionType": "BypassCondition",
                "pattern": "::1"
            }},
            {{
                "conditionType": "BypassCondition",
                "pattern": "localhost"
            }}
        ],
        "color": "{node_color}",
        "fallbackProxy": {{
            "host": "127.0.0.1",
            "port": {node_port},
            "scheme": "socks5"
        }},
        "name": "{node_name}",
        "profileType": "FixedProfile",
        "revision": "{node_revision}"
    }},
"""

def omega_color_pick():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

def omega_random_revision():
    return ''.join([random.choice('0123456789abcdef') for j in range(11)])

def omega_make_proxy_node(name, port):
    return OMEGA_PROXY_PATTERN.format(
        node_name=name, node_color=omega_color_pick(),
        node_revision=omega_random_revision(), node_port=port
    )

# "OmegaSwitch.json"
def generate(name, list_of_name_port_pairs):
    with open(name, "w") as f:
        f.write("{\n")
        for pair in list_of_name_port_pairs:
            f.write(omega_make_proxy_node(pair[0], pair[1]))
        f.write(OMEGA_COMMON_TONGUE)
        f.write("}\n")

# "OmegaSwitch.json"
def generate_for_windows(name):
    with open(name, "w") as f:
        f.write("{\n")
        f.write(omega_make_proxy_node("FUCKGFW", 10800))
        f.write(OMEGA_COMMON_TONGUE)
        f.write("}\n")