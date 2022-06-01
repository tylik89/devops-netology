import socket
import time
import json
import yaml


hosts = {"drive.google.com": "", "mail.google.com": "", "google.com": ""}
while True:
    for url, ip in hosts.items():
        ip_addr = socket.gethostbyname(url)
        if ip == "":
            hosts[url] = ip_addr
            print(f'{url} - {ip_addr}')
        elif ip != ip_addr:
            print(f'[ERROR] {url} IP mismatch: {ip} -> {ip_addr}')
            hosts[url] = ip_addr
    with open('hosts.json', 'w') as json_file:
        json_file.write(json.dumps(hosts, indent=2))
    with open('hosts.yaml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(hosts, indent=2, explicit_start=True, explicit_end=True))
    time.sleep(1)