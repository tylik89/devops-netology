# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
   
   Нужно найти и исправить все ошибки, которые допускает наш сервис

 ```json
{
  "info": "Sample JSON output from our service\t",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": 7175
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
```


2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

```python
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
```

```shell
//usr/bin/python3.10 /home/a1/web/devops-netology/04-script-03-yaml/script_03.py
drive.google.com - 64.233.162.194
mail.google.com - 64.233.164.18
google.com - 108.177.14.102
[ERROR] google.com IP mismatch: 108.177.14.102 -> 108.177.14.138
[ERROR] mail.google.com IP mismatch: 64.233.164.18 -> 64.233.164.19
[ERROR] google.com IP mismatch: 108.177.14.138 -> 108.177.14.139
[ERROR] google.com IP mismatch: 108.177.14.139 -> 108.177.14.138
[ERROR] mail.google.com IP mismatch: 64.233.164.19 -> 64.233.164.83
[ERROR] google.com IP mismatch: 108.177.14.138 -> 108.177.14.113
[ERROR] mail.google.com IP mismatch: 64.233.164.83 -> 64.233.164.18
[ERROR] google.com IP mismatch: 108.177.14.113 -> 108.177.14.101
```