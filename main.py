import omega
import interact
import gui_config
import copy
import systemctl

if __name__ == "__main__":
    port, passwd, list_of_host_method_pair = interact.eat()
    # create gui_config.json
    gui_config.generate(port, passwd, list_of_host_method_pair)
    # on linux, ss service ports start from 1090
    ss_port = 1090
    list_of_hosts_port_pair_linux = []
    for each in list_of_host_method_pair:
        list_of_hosts_port_pair_linux.append((each[0], ss_port))
        ss_port += 1
    omega.generate("out/OmegaSwitchLinux.json", list_of_hosts_port_pair_linux)
    omega.generate_for_windows("out/OmegaSwitchWin.json")
    ##  systemctl service file
    list_of_ss_config = []
    ss_port = 1090
    for each in list_of_host_method_pair:
        ssconfig = systemctl.ssconfig(each[0], port, ss_port, passwd, each[1])
        list_of_ss_config.append(ssconfig)
        ss_port += 1
    
    systemctl.ss_generate(list_of_ss_config)


