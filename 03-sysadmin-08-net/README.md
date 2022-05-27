# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP
```
telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32
```
```shell
route-views>show ip route 185.233.202.85 
Routing entry for 185.233.202.0/23
  Known via "bgp 6447", distance 20, metric 0
  Tag 3333, type external
  Last update from 193.0.0.56 2w1d ago
  Routing Descriptor Blocks:
  * 193.0.0.56, from 193.0.0.56, 2w1d ago
      Route metric is 0, traffic share count is 1
      AS Hops 3
      Route tag 3333
      MPLS label: none
route-views>show bgp 185.233.202.85
BGP routing table entry for 185.233.202.0/23, version 2289820057
Paths: (24 available, best #14, table default)
  Not advertised to any peer
  Refresh Epoch 1
  8283 56630 200740
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 8283:1 8283:101 8283:102 56630:9001 56630:43120 56630:56630
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x24
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 0000 205B 0000 0005
              0000 0002 
      path 7FE0BDE36F20 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  53767 174 56630 200740
    162.251.163.2 from 162.251.163.2 (162.251.162.3)
      Origin IGP, localpref 100, valid, external
      Community: 174:21101 174:22010 53767:5000
      path 7FE113868BC8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  19214 3257 56630 200740
    208.74.64.40 from 208.74.64.40 (208.74.64.40)
      Origin IGP, localpref 100, valid, external
      Community: 3257:4000 3257:8793 3257:50001 3257:50110 3257:53100 3257:53101
      path 7FE0192F74D8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3549 3356 56630 200740
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067 3549:2581 3549:30840 56630:9001 56630:43120 56630:56630
      path 7FE055D6EB60 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  701 3356 56630 200740
    137.39.3.55 from 137.39.3.55 (137.39.3.55)
      Origin IGP, localpref 100, valid, external
      path 7FE187B98348 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 56630 200740
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067 56630:9001 56630:43120 56630:56630
      path 7FE0B649BC48 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 3910 3356 56630 200740
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE14218EB48 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  57866 3356 56630 200740
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067 56630:9001 56630:43120 56630:56630
      path 7FE113A88948 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 3356 56630 200740
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin IGP, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE17DE0FC08 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 3257 56630 200740
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin IGP, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE170CA1CA8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20912 174 56630 200740
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin IGP, localpref 100, valid, external
      Community: 174:21101 174:22010 20912:65002
      path 7FE177C2DF48 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3267 56630 200740
    194.85.40.15 from 194.85.40.15 (185.141.126.1)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE12C73B828 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 56630 200740
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external
      path 7FE15E855C28 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 56630 200740
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external, best
      Community: 56630:9001 56630:43120 56630:56630
      path 7FE0C8C236A8 RPKI State valid
      rx pathid: 0, tx pathid: 0x0
  Refresh Epoch 1
  101 2914 56630 200740
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20100 101:20110 101:22100 2914:410 2914:1206 2914:2203 2914:3200 56630:9001 56630:43120 56630:56630
      Extended Community: RT:101:22100
      path 7FE04825F840 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 56630 200740
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE18546EF28 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  852 3356 56630 200740
    154.11.12.212 from 154.11.12.212 (96.1.209.43)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE16D1D7890 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 56630 200740
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE1485D1BF0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3303 3356 56630 200740
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1004 3303:1006 3303:3051 3356:2 3356:22 3356:100 3356:123 3356:503 3356:901 3356:2067 3356:10037 56630:9001 56630:43120 56630:56630
      path 7FE09F6B5908 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 2
  2497 3257 56630 200740
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin IGP, localpref 100, valid, external
      path 7FE13DDCF728 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7660 2516 3257 56630 200740
    203.181.248.168 from 203.181.248.168 (203.181.248.168)
      Origin IGP, localpref 100, valid, external
      Community: 2516:1030 7660:9001
      path 7FE050DFD140 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 12552 56630 200740
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin IGP, localpref 100, valid, external
      Community: 12552:12000 12552:12700 12552:12701 12552:22000
      Extended Community: 0x43:100:1
      path 7FE14FF0CBC8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1221 4637 3257 56630 200740
    203.62.252.83 from 203.62.252.83 (203.62.252.83)
      Origin IGP, localpref 100, valid, external
      path 7FE0A3DB1090 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3257 56630 200740
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin IGP, metric 10, localpref 100, valid, external
      Community: 3257:4000 3257:8793 3257:50001 3257:50110 3257:53100 3257:53101
      path 7FE02431D728 RPKI State valid
      rx pathid: 0, tx pathid: 0

```
---
2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

Создаем dummy-интерфейс:
```shell
echo "dummy" >> /etc/modules
echo "options dummy numdummies=2" > /etc/modprobe.d/dummy.conf
vim /etc/network/interfaces
auto dummy0
iface dummy0 inet static    
  address 10.2.2.2/32    
  pre-up ip link add dummy0 type dummy
  post-down ip link del dummy0
```
Далее перезапуск ОС для загрузки ядра ядра. Проверяем после загрузки ОС состояние dummy-interface и добавим несколько статических маршрутов

```shell
root@a1:~# ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp0s3           UP             10.0.2.15/24 fe80::c186:1751:8c66:b060/64 
dummy0           UNKNOWN        10.2.2.2/32 fe80::2098:e1ff:fe42:9d97/64 

root@a1:~# ip route add 192.168.1.0/24 via 10.0.2.15
root@a1:~# ip route add 192.168.2.0/24 dev enp0s3 

root@a1:~# ip -br r
default via 10.0.2.2 dev enp0s3 proto dhcp metric 100 
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 metric 100 
169.254.0.0/16 dev dummy0 scope link metric 1000 
192.168.1.0/24 via 10.0.2.15 dev enp0s3 
192.168.2.0/24 dev enp0s3 scope link 
```
---
3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

```shell
root@a1:~# ss -ltpan
State              Recv-Q          Send-Q                        Local Address:Port                          Peer Address:Port           Process                                                            
LISTEN             0               4096                                0.0.0.0:51957                              0.0.0.0:*               users:(("rpc.statd",pid=1209,fd=9))                               
LISTEN             0               4096                          127.0.0.53%lo:53                                 0.0.0.0:*               users:(("systemd-resolve",pid=608,fd=14))                         
LISTEN             0               64                                  0.0.0.0:33783                              0.0.0.0:*                                                                                 
LISTEN             0               128                               127.0.0.1:631                                0.0.0.0:*               users:(("cupsd",pid=1026,fd=7))                                   
LISTEN             0               64                                  0.0.0.0:2049                               0.0.0.0:*                                                                                 
LISTEN             0               4096                                0.0.0.0:33377                              0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=13))                             
LISTEN             0               4096                                0.0.0.0:51905                              0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=5))                              
LISTEN             0               4096                                0.0.0.0:59173                              0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=9))                              
LISTEN             0               4096                                0.0.0.0:111                                0.0.0.0:*               users:(("rpcbind",pid=606,fd=4),("systemd",pid=1,fd=35))          
ESTAB              0               0                                 127.0.0.1:59914                            127.0.0.1:63342           users:(("jcef_helper",pid=2970,fd=23))                            
SYN-SENT           0               1                                 10.0.2.15:44646                        138.68.92.190:443             users:(("chrome",pid=4546,fd=32))                                 
ESTAB              0               0                                 10.0.2.15:36346                       173.194.221.95:443             users:(("chrome",pid=4546,fd=36))                                 
TIME-WAIT          0               0                                 10.0.2.15:59046                      142.250.150.102:443                                                                               
ESTAB              0               0                                 10.0.2.15:51850                      142.250.150.139:443             users:(("chrome",pid=4546,fd=40))                                 
TIME-WAIT          0               0                                 10.0.2.15:46210                        74.125.131.95:443                                                                               
TIME-WAIT          0               0                                 10.0.2.15:33130                        64.233.163.83:443                                                                               
ESTAB              0               0                                 10.0.2.15:48760                       173.194.222.94:443             users:(("chrome",pid=4546,fd=22))                                 
TIME-WAIT          0               0                                 10.0.2.15:52094                       173.194.221.94:443                                                                               
ESTAB              0               0                                 10.0.2.15:34436                        74.125.131.94:443             users:(("chrome",pid=4546,fd=43))                                 
TIME-WAIT          0               0                                 10.0.2.15:55694                        173.194.73.95:443                                                                               
TIME-WAIT          0               0                                 10.0.2.15:51410                       209.85.233.100:443                                                                               
TIME-WAIT          0               0                                 10.0.2.15:37458                       142.250.150.84:443                                                                               
ESTAB              0               0                                 10.0.2.15:37660                       64.233.161.188:5228            users:(("chrome",pid=4546,fd=51))                                 
ESTAB              0               0                                 10.0.2.15:33622                         142.251.1.83:443             users:(("chrome",pid=4546,fd=31))                                 
TIME-WAIT          0               0                                 10.0.2.15:44726                       64.233.161.147:443                                                                               
LISTEN             0               128                                   [::1]:631                                   [::]:*               users:(("cupsd",pid=1026,fd=6))                                   
LISTEN             0               4096                                   [::]:56665                                 [::]:*               users:(("rpc.statd",pid=1209,fd=11))                              
LISTEN             0               4096                                   [::]:33595                                 [::]:*               users:(("rpc.mountd",pid=1214,fd=15))                             
LISTEN             0               4096                                   [::]:54299                                 [::]:*               users:(("rpc.mountd",pid=1214,fd=11))                             
LISTEN             0               4096                     [::ffff:127.0.0.1]:6942                                     *:*               users:(("java",pid=2803,fd=27))                                   
LISTEN             0               64                                     [::]:37537                                 [::]:*                                                                                 
LISTEN             0               64                                     [::]:2049                                  [::]:*                                                                                 
LISTEN             0               4096                                   [::]:47719                                 [::]:*               users:(("rpc.mountd",pid=1214,fd=7))                              
LISTEN             0               4096                     [::ffff:127.0.0.1]:63342                                    *:*               users:(("java",pid=2803,fd=40))                                   
LISTEN             0               4096                                   [::]:111                                   [::]:*               users:(("rpcbind",pid=606,fd=6),("systemd",pid=1,fd=37))          
ESTAB              0               0                        [::ffff:127.0.0.1]:63342                   [::ffff:127.0.0.1]:59914           users:(("java",pid=2803,fd=120)) 


```
* 22/TCP,UDP	SSH (Secure SHell) — криптографический сетевой протокол для безопасной передачи данных
* 53/TCP,UDP	DOMAIN (Domain Name System, DNS)
* 68/TCP,UDP	BOOTPC (Bootstrap Protocol Client) — для клиентов бездисковых рабочих станций, загружающихся с сервера BOOTP; также используется DHCP (Dynamic Host Configuration Protocol)
* 80/TCP,UDP	HTTP (HyperText Transfer Protocol)
* 111/TCP,UDP	SUNRPC (Sun Remote Procedure Call
* 443/TCP,UDP	HTTPS (HyperText Transfer Protocol Secure) — HTTP с шифрованием по SSL или TLS
* 631/TCP,UDP	IPP (Internet Printing Protocol)

4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

```shell
root@a1:~# ss -lupan
State            Recv-Q           Send-Q                          Local Address:Port                        Peer Address:Port           Process                                                             
UNCONN           0                0                                     0.0.0.0:57109                            0.0.0.0:*               users:(("avahi-daemon",pid=714,fd=14))                             
UNCONN           0                0                               127.0.0.53%lo:53                               0.0.0.0:*               users:(("systemd-resolve",pid=608,fd=13))                          
ESTAB            0                0                            10.0.2.15%enp0s3:68                              10.0.2.2:67              users:(("NetworkManager",pid=721,fd=25))                           
UNCONN           0                0                                     0.0.0.0:111                              0.0.0.0:*               users:(("rpcbind",pid=606,fd=5),("systemd",pid=1,fd=36))           
UNCONN           0                0                                     0.0.0.0:631                              0.0.0.0:*               users:(("cups-browsed",pid=1199,fd=7))                             
UNCONN           0                0                                   127.0.0.1:961                              0.0.0.0:*               users:(("rpc.statd",pid=1209,fd=5))                                
UNCONN           0                0                                     0.0.0.0:50369                            0.0.0.0:*                                                                                  
UNCONN           0                0                                     0.0.0.0:60452                            0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=4))                               
UNCONN           0                0                                     0.0.0.0:37673                            0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=12))                              
UNCONN           0                0                                     0.0.0.0:54497                            0.0.0.0:*               users:(("rpc.statd",pid=1209,fd=8))                                
UNCONN           0                0                                 224.0.0.251:5353                             0.0.0.0:*               users:(("chrome",pid=4499,fd=263))                                 
UNCONN           0                0                                 224.0.0.251:5353                             0.0.0.0:*               users:(("chrome",pid=4499,fd=262))                                 
UNCONN           0                0                                     0.0.0.0:5353                             0.0.0.0:*               users:(("avahi-daemon",pid=714,fd=12))                             
UNCONN           0                0                                     0.0.0.0:56117                            0.0.0.0:*               users:(("rpc.mountd",pid=1214,fd=8))                               
UNCONN           0                0                                        [::]:111                                 [::]:*               users:(("rpcbind",pid=606,fd=7),("systemd",pid=1,fd=38))           
UNCONN           0                0                                        [::]:58884                               [::]:*               users:(("rpc.statd",pid=1209,fd=10))                               
UNCONN           0                0                                        [::]:51762                               [::]:*                                                                                  
UNCONN           0                0                                        [::]:43991                               [::]:*               users:(("rpc.mountd",pid=1214,fd=10))                              
UNCONN           0                0                                        [::]:36255                               [::]:*               users:(("rpc.mountd",pid=1214,fd=6))                               
UNCONN           0                0                                        [::]:44551                               [::]:*               users:(("avahi-daemon",pid=714,fd=15))                             
UNCONN           0                0                                        [::]:5353                                [::]:*               users:(("avahi-daemon",pid=714,fd=13))                             
UNCONN           0                0                                        [::]:55527                               [::]:*               users:(("rpc.mountd",pid=1214,fd=14))                 
```


5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали. 

![network](img/home.drawio.png)

 ---