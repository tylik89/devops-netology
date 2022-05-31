## Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?

в Linux  `ip -br link`

```shell
a1@a1:~$ ip -c -br link
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
enp0s3           UP             08:00:27:2a:9c:95 <BROADCAST,MULTICAST,UP,LOWER_UP> 
cl1              UNKNOWN        <POINTOPOINT,NOARP,UP,LOWER_UP> 
```
в Windows `netsh interface show interface` или `ipconfig /all`
```shell
C:\Users\tylik_a>netsh interface show interface

Состояние адм.  Состояние     Тип              Имя интерфейса
---------------------------------------------------------------------
Разрешен       Отключен       Выделенный       Ethernet 2
Разрешен       Подключен      Выделенный       VirtualBox Host-Only Network
Разрешен       Подключен      Выделенный       Ethernet
Разрешен       Отключен       Выделенный       Беспроводная сеть
   ```

---
2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?

Link Layer Discovery Protocol (LLDP) —  протокол канального уровня, который позволяет сетевым устройствам 
анонсировать в сеть информацию о себе и о своих возможностях,
а также собирать эту информацию о соседних устройствах. 
Пакет lldpd 
```shell
1@a1:~$ lldpctl
-------------------------------------------------------------------------------
LLDP neighbors:
-------------------------------------------------------------------------------
```
---
3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.

Технология VLAN (аббр. от англ. Virtual Local Area Network) — виртуальная локальная компьютерная сеть. 
Представляет собой группу хостов с общим набором требований, которые взаимодействуют так, как если бы они были 
подключены к широковещательному домену независимо от их физического местонахождения.
VLAN имеет те же свойства, что и физическая локальная сеть, но позволяет конечным членам группироваться вместе, 
даже если они не находятся в одной физической сети. Такая реорганизация может быть сделана на основе программного 
обеспечения вместо физического перемещения устройств.

```shell
root@a1:~# ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             10.0.2.15/24 fe80::c186:1751:8c66:b060/64 
cl1              UNKNOWN        10.6.0.2/24 
root@a1:~# ip link add link enp0s3  name enp0s3.16 type vlan id 16
root@a1:~# ip address add 10.0.2.16/24 dev enp0s3.16
root@a1:~# ip link set enp0s3.16 up
root@a1:~# ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             10.0.2.15/24 fe80::c186:1751:8c66:b060/64 
cl1              UNKNOWN        10.6.0.2/24 
enp0s3.16@enp0s3 UP             10.0.2.16/24 fe80::a00:27ff:fe2a:9c95/64 
root@a1:~# ip link delete enp0s3.16
root@a1:~# ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             10.0.2.15/24 fe80::c186:1751:8c66:b060/64 
cl1              UNKNOWN        10.6.0.2/24 
```
---
4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.

   * LACP (link aggregation control protocol) стандартный протокол
   * PAgP (Port Aggregation Protoco) проприетарный протокол Cisco
   * Статическое агрегирование без использования протоколов  
   Из основных опций для балансировки:
   * balance-rr  (mode=0): Данный режим используется по умолчанию. Balance-rr обеспечивается балансировку нагрузки и отказоустойчивость. В данном режиме сетевые пакеты отправляются “по кругу”, от первого интерфейса к последнему. Если выходят из строя интерфейсы, пакеты отправляются на остальные оставшиеся. Дополнительной настройки коммутатора не требуется при нахождении портов в одном коммутаторе. При разностных коммутаторах требуется дополнительная настройка.
   * active-backup  (mode=1): Только один ведомый активен в единицу времени. Второй ведомый активируется после осени с первым ведомым. Данный режим запрашивается только отказоустойчивость.
   * balance-xor (mode=2): Применяется хэш-политика в виде MAC-источника XOR MAC-получателя. Данный режим требует отказоустойчивости и балансировки нагрузки.
   * broadcast (mode=3): Передача идёт через все интерфейсы. Данный режим обеспечивает  только отказоустойчивость.
   * 802.3ad (mode=4): Должен применяться только если контакт поддерживает IEEE 802.3ad Агрегация динамических ссылок.
   * balance-tlb (mode=5): Не требуется поддержка со стороны обращения. Исходящий трафик зависит от нагрузки каждого ведомого. Входящий трафик привлекается к ведомому, и если он отказывает, то другой ведомый берет работу на себя.
   * balance-alb (mode=6): alb - Адаптивная балансировка нагрузки. Работает как balance-tlb + балансировка нагрузки rlb для IPv4.  

Пример настройки интерфейсов eth0 и eth1 в режиме active-backup в файле «/etc/network/interfaces»:
```shell
auto bond0
iface bond0 inet dhcp
   bond-slaves eth0 eth1
   bond-mode active-backup
   bond-miimon 100
   bond-primary eth0 eth1
```

---
5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.

в сети с маской /29  8 ip адресов (6 хостов 1 броадкаст и 1 сеть)    
```shell
root@a1:~# ipcalc 10.10.10.0/29  
Address:   10.10.10.0           00001010.00001010.00001010.00000 000
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000
Wildcard:  0.0.0.7              00000000.00000000.00000000.00000 111
=>
Network:   10.10.10.0/29        00001010.00001010.00001010.00000 000
HostMin:   10.10.10.1           00001010.00001010.00001010.00000 001
HostMax:   10.10.10.6           00001010.00001010.00001010.00000 110
Broadcast: 10.10.10.7           00001010.00001010.00001010.00000 111
Hosts/Net: 6                     Class A, Private Internet

```
 31-подсеть можно получить с маской /29  можно получить из сети с маской /24
```shell
root@a1:~# ipcalc -s 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 10.10.10.0/24
Address:   10.10.10.0           00001010.00001010.00001010. 00000000
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111
=>
Network:   10.10.10.0/24        00001010.00001010.00001010. 00000000
HostMin:   10.10.10.1           00001010.00001010.00001010. 00000001
HostMax:   10.10.10.254         00001010.00001010.00001010. 11111110
Broadcast: 10.10.10.255         00001010.00001010.00001010. 11111111
Hosts/Net: 254                   Class A, Private Internet

1. Requested size: 6 hosts
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000
Network:   10.10.10.0/29        00001010.00001010.00001010.00000 000
HostMin:   10.10.10.1           00001010.00001010.00001010.00000 001
HostMax:   10.10.10.6           00001010.00001010.00001010.00000 110
Broadcast: 10.10.10.7           00001010.00001010.00001010.00000 111
Hosts/Net: 6                     Class A, Private Internet

2. Requested size: 6 hosts
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000
Network:   10.10.10.8/29        00001010.00001010.00001010.00001 000
HostMin:   10.10.10.9           00001010.00001010.00001010.00001 001
HostMax:   10.10.10.14          00001010.00001010.00001010.00001 110
Broadcast: 10.10.10.15          00001010.00001010.00001010.00001 111
Hosts/Net: 6                     Class A, Private Internet
....

32. Requested size: 6 hosts
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000
Network:   10.10.10.248/29      00001010.00001010.00001010.11111 000
HostMin:   10.10.10.249         00001010.00001010.00001010.11111 001
HostMax:   10.10.10.254         00001010.00001010.00001010.11111 110
Broadcast: 10.10.10.255         00001010.00001010.00001010.11111 111
Hosts/Net: 6                     Class A, Private Internet

Needed size:  256 addresses.
Used network: 10.10.10.0/24
Unused:
```
---
6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.

возьмем сеть 100.64.0.64/26
```shell
root@a1:~# ipcalc -s 50 100.64.0.0/10
Address:   100.64.0.0           01100100.01 000000.00000000.00000000
Netmask:   255.192.0.0 = 10     11111111.11 000000.00000000.00000000
Wildcard:  0.63.255.255         00000000.00 111111.11111111.11111111
=>
Network:   100.64.0.0/10        01100100.01 000000.00000000.00000000
HostMin:   100.64.0.1           01100100.01 000000.00000000.00000001
HostMax:   100.127.255.254      01100100.01 111111.11111111.11111110
Broadcast: 100.127.255.255      01100100.01 111111.11111111.11111111
Hosts/Net: 4194302               Class A

1. Requested size: 50 hosts
Netmask:   255.255.255.224 = 27 11111111.11111111.11111111.111 00000
Network:   100.64.0.0/27        01100100.01000000.00000000.000 00000
HostMin:   100.64.0.1           01100100.01000000.00000000.000 00001
HostMax:   100.64.0.30          01100100.01000000.00000000.000 11110
Broadcast: 100.64.0.31          01100100.01000000.00000000.000 11111
Hosts/Net: 30                    Class A

Needed size:  64 addresses.
Used network: 100.64.0.0/26
Unused:
100.64.0.64/26
100.64.0.128/25
100.64.1.0/24
100.64.2.0/23
100.64.4.0/22
100.64.8.0/21
100.64.16.0/20
100.64.32.0/19
100.64.64.0/18
100.64.128.0/17
100.65.0.0/16
100.66.0.0/15
100.68.0.0/14
100.72.0.0/13
100.80.0.0/12
100.96.0.0/11
```

---
7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?

 в Windows: 
для просмотра ARP-таблицы используем `arp -a`:  
```shell
C:\Users\tylik_a>arp -a

Интерфейс: 192.168.56.1 --- 0x12
  адрес в Интернете      Физический адрес      Тип
  192.168.56.255        ff-ff-ff-ff-ff-ff     статический
  224.0.0.22            01-00-5e-00-00-16     статический
  224.0.0.251           01-00-5e-00-00-fb     статический
  224.0.0.252           01-00-5e-00-00-fc     статический
  239.255.255.250       01-00-5e-7f-ff-fa     статический
  255.255.255.255       ff-ff-ff-ff-ff-ff     статический

Интерфейс: 10.150.2.93 --- 0x13
  адрес в Интернете      Физический адрес      Тип
  10.150.2.1            e4-c7-22-d0-7d-70     динамический
  10.150.2.75           04-92-26-cd-de-3a     динамический
  10.150.2.91           04-d9-f5-ce-89-92     динамический
  10.150.2.255          ff-ff-ff-ff-ff-ff     статический
  224.0.0.22            01-00-5e-00-00-16     статический
  224.0.0.251           01-00-5e-00-00-fb     статический
  224.0.0.252           01-00-5e-00-00-fc     статический
  239.255.255.250       01-00-5e-7f-ff-fa     статический
  255.255.255.255       ff-ff-ff-ff-ff-ff     статический
```
для очистки кеша ARP-таблицы используем `arp -d *`.  
для удаления из ARP-таблицы одного IP используем `arp -d 192.168.56.255`, указав конкретный ip-адрес.  

в Linux:

для просмотра ARP-таблицы используем `arp -a` (BSD style output format (with no fixed columns) или `arp -e` (Linux style output format (with fixed columns)):  
```shell
root@a1:~# arp -a
_gateway (10.0.2.2) в 52:54:00:12:35:02 [ether] на enp0s3


root@a1:~# arp -e
Адрес HW-тип HW-адрес Флаги Маска Интерфейс
_gateway                 ether   52:54:00:12:35:02   C                     enp0s3
```
для очистки кеша ARP-таблицы используем `ip neigh flush all`:  
для удаления из ARP-таблицы одного IP используем `arp -d 10.0.2.2`, указав конкретный ip-адрес. 

---