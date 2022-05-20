# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

1. На лекции мы познакомились с [node_exporter](https://github.com/prometheus/node_exporter/releases). В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой [unit-файл](https://www.freedesktop.org/software/systemd/man/systemd.service.html) для node_exporter:

    * поместите его в автозагрузку,
    * предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на `systemctl cat cron`),
    * удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.

```shell
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz
tar xvfz node_exporter-1.3.1.linux-amd64.tar.gz 
sudo cp -r node_exporter-1.3.1.linux-amd64 /usr/local/bin/ 
предусмортрим возможность добавления опций к запускаемому процессу через внешний файл
~$ cat /opt/node_exporter.env 
EXTRA_OPTS="--log.level=info"
создадим Файл конфигурации модуля
[Unit]
Description= Node Exporter  
After=network.target  
   
[Service]  
Type=simple  
EnvironmentFile=/opt/node_exporter.env 
ExecStart=/usr/local/bin/node_exporter-1.3.1.linux-amd64/node_exporter  $EXTRA_OPTS
   
[Install]  
WantedBy=multi-user.target 

запустим службу 

vagrant@vagrant:~$ sudo systemctl daemon-reload
vagrant@vagrant:~$ sudo systemctl start node_exporter
vagrant@vagrant:~$ sudo systemctl enable node_exporter
Created symlink /etc/systemd/system/multi-user.target.wants/node_exporter.service → /etc/systemd/system/node_exporter.service.
vagrant@vagrant:~$ sudo systemctl status node_exporter
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2022-05-19 07:32:08 UTC; 52s ago
   Main PID: 1492 (node_exporter)
      Tasks: 5 (limit: 1071)
     Memory: 2.7M
     CGroup: /system.slice/node_exporter.service
             └─1492 /usr/local/bin/node_exporter-1.3.1.linux-amd64/node_exporter --log.level=info

проверим после перезагрузки 

vagrant@vagrant:~$ exit 
logout
Connection to 127.0.0.1 closed.
a1@a1:~/03-sysadmin-04$ vagrant reload
...
vagrant@vagrant:~$ sudo systemctl status node_exporter
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2022-05-19 07:44:56 UTC; 1min 53s ago
   Main PID: 613 (node_exporter)
      Tasks: 4 (limit: 1071)
     Memory: 14.3M
     CGroup: /system.slice/node_exporter.service
             └─613 /usr/local/bin/node_exporter-1.3.1.linux-amd64/node_exporter --log.level=info

```
---
2. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.

Процессор
 ```
  node_cpu_seconds_total{cpu="0",mode="idle"} 5026.4
  node_cpu_seconds_total{cpu="0",mode="system"} 56.58
  node_cpu_seconds_total{cpu="0",mode="user"} 4.84
  node_cpu_seconds_total{cpu="1",mode="idle"} 5025.01
  node_cpu_seconds_total{cpu="1",mode="system"} 13.46
  node_cpu_seconds_total{cpu="1",mode="user"} 1.61
  process_cpu_seconds_total 3
 ```
 
Oбъем памяти
  ```
  node_memory_MemTotal_bytes 1.028694016e+09
  node_memory_MemFree_bytes 5.68066048e+08
  node_memory_MemAvailable_bytes 7.6163072e+08
  node_memory_Buffers_bytes 2.3498752e+07
  node_memory_Cached_bytes 2.90205696e+08 
  ```
Диск
  ```
  node_disk_io_time_seconds_total{device="sda"} 12.012
  node_disk_read_bytes_total{device="sda"} 3.16904448e+08
  node_disk_read_time_seconds_total{device="sda"} 7.303
  node_disk_written_bytes_total{device="sda"} 7.4236928e+07
  node_disk_write_time_seconds_total{device="sda"} 7.746
  ```
Сеть
  ```
  node_network_receive_bytes_total{device="eth0"} 545686
  node_network_receive_errs_total{device="eth0"} 0
  node_network_transmit_bytes_total{device="eth0"} 434942
  node_network_transmit_errs_total{device="eth0"} 0
  ```
---
3. Установите в свою виртуальную машину [Netdata](https://github.com/netdata/netdata). Воспользуйтесь [готовыми пакетами](https://packagecloud.io/netdata/netdata/install) для установки (`sudo apt install -y netdata`). После успешной установки:
    * в конфигурационном файле `/etc/netdata/netdata.conf` в секции [web] замените значение с localhost на `bind to = 0.0.0.0`,
    * добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте `vagrant reload`:

    ```bash
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    ```

    После успешной перезагрузки в браузере *на своем ПК* (не в виртуальной машине) вы должны суметь зайти на `localhost:19999`. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.
![Netdata](3.png)
---

4. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?
 
да, можно
```
vagrant@vagrant:~$ dmesg 
[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
[    0.000000] Hypervisor detected: KVM
[    0.006525] CPU MTRRs all blank - virtualized system.
[    0.398245] Booting paravirtualized kernel on KVM
[   22.228574] systemd[1]: Detected virtualization oracle.
```

---
5. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?

`fs.nr_open`- лимит на количество открытых дескрипторов ядра системы 

```
vagrant@vagrant:~$ sysctl -n fs.nr_open
1048576
```
`ulimit -n` - максимальное количество активных файлов дескрипторов (большинство систем не позволяет использовать это значение)
`ulimit -Hn`- жесткое отказ после установки превосходить нельзя; 
`ulimit -Sn`- мягко упустить можно превосходить до значения очень жесткого ограничения.

---
6. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.

---
7. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?

 
---




