import re
def eat():
    port = 0
    password = ""
    list_of_domain_method_pair = []
    while True:
        try:
            x = input()
            if len(x):
                if x.startswith("ShadowSocks Port"):
                    port = int(x.replace("ShadowSocks Port", ""))
                elif x.startswith("ShadowSocks Password"):
                    password = x.strip().replace("ShadowSocks Password", "")
                elif "|" in x:
                    foo = x.split('|')
                    domain = foo[0].strip()
                    encryption = foo[1].strip()
                    if "aes" in encryption:
                        e2 = re.search(r"aes-[\w]*-[\w]*", encryption)
                        list_of_domain_method_pair.append((domain, e2.group()))

        except EOFError:
            break
    return port, password, list_of_domain_method_pair