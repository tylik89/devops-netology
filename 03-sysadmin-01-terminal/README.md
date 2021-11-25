# Домашнее задание к занятию "3.1. Работа в терминале, лекция 1"

1. Устаннавливаем средство виртуализации [Oracle VirtualBox](https://www.virtualbox.org/)  из репозиториев Oracle

Чтобы установить VirtualBox из репозиториев Oracle, выполним следующие действия:

1.1 Импортируйте открытые ключи Oracle с помощью следующих команд:
```bash
 $ wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
 
 $ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```
Обе команды должны вывести OK , что означает, что ключи успешно импортированы, и пакеты из этого репозитория будут считаться доверенными.

1.2 Добавим репозиторий VirtualBox APT в систему:
```bash
 $ echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | 
 sudo tee -a /etc/apt/sources.list.d/virtualbox.list
```
$(lsb_release -cs) выводит кодовое имя Ubuntu. Например, если у вас Ubuntu версии 20.04, команда напечатает focal .

1.3 Обновим список пакетов и установите последнюю версию VirtualBox:
```bash
$ sudo apt update
 
$ sudo apt install virtualbox-6.1
```

2. Установим средство автоматизации [Hashicorp Vagrant](https://www.vagrantup.com/).

Чтобы установить  Vagrant на  Ubuntu , выполниним следующие действия:
```bash
$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -

$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

$ sudo apt-get update && sudo apt-get install vagrant
```

3. В основном окружении подготовим GNOME Terminal  для дальнейшей работы ознокомимся с [документацией](https://help.ubuntu.ru/wiki/gnome_terminal)
 

4. С помощью базового файла конфигурации запустим Ubuntu 20.04 в VirtualBox посредством Vagrant:

    * Создайте директорию, в которой будут храниться конфигурационные файлы Vagrant. В ней выполните `vagrant init`. Замените содержимое Vagrantfile по умолчанию следующим:

        ```bash
        Vagrant.configure("2") do |config|
            config.vm.box = "bento/ubuntu-20.04"
        end
        ```
    [Vagrantfile](Vagrantfile) 

    * Выполненим в этой директории `vagrant up` установит провайдер VirtualBox для Vagrant, скачает необходимый образ и запустит виртуальную машину.

    * `vagrant suspend` выключит виртуальную машину с сохранением ее состояния (т.е., при следующем `vagrant up` будут запущены все процессы внутри, которые работали на момент вызова suspend), `vagrant halt` выключит виртуальную машину штатным образом.

5. Ознакомьтесь с графическим интерфейсом VirtualBox, посмотрим как выглядит виртуальная машина, которую создал Vagrant ![VM](img/VM.png)
этой машине выделено: 
* 1024 МБ Оперативной памити 
* 2 процессора 
* 64 ГБ жестгого диска 


6. Ознакомися с возможностями конфигурации VirtualBox через Vagrantfile: [документация](https://www.vagrantup.com/docs/providers/virtualbox/configuration.html).

Добавить оперативной памяти или ресурсов процессора виртуальной машине можно так:

```bash
  config.vm.provider "virtualbox" do |vb|
          # объем оперативной памяти
          vb.memory = 2048
          # количество ядер процессора
          vb.cpus = 4
  end
```

7. Команда `vagrant ssh` из директории, в которой содержится Vagrantfile, позволит вам оказаться внутри виртуальной машины без каких-либо дополнительных настроек. Попрактикуйтесь в выполнении обсуждаемых команд в терминале Ubuntu.
```bash
~/devops-netology/03-sysadmin-01-terminal$ vagrant ssh
echo Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-80-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed 24 Nov 2021 01:26:21 PM UTC

  System load:  0.2               Processes:             106
  Usage of /:   2.4% of 61.31GB   Users logged in:       0
  Memory usage: 14%               IPv4 address for eth0: 10.0.2.15
  Swap usage:   0%


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
vagrant@vagrant:~$ 
```
8. Ознакомимся  с разделами `man bash`, почитать о настройках самого bash:
    * $HISTSIZE  можно задать длину журнала `history`, и это написано на 966 строке manual
    * директива ignoreboth в переменной HISTCONTROL включает директивы ignorespace и ignoredups, т.е. в истории не будут сохраняться команды, начинающиеся с пробела, а также команды, которые уже сохранены в истории

9. В каких сценариях использования применимы скобки `{}` и на какой строчке `man bash` это описано?

* с помощью фигурных скобок можно выполнить одну команду несколько раз с разными параметрами, написано на 281 строке
10. Чтобы содать 100000 файлов одновремено воспользуемся командой `touch {1..100000}`, 
но при создании 300000 файлов командной строки мы увидим на экране следующее сообщение об ошибке:
```bash
$ touch {1..300000}
-bash: /usr/bin/touch: Argument list too long
```
Все оболочки имеют ограничение на длину командной строки. Система UNIX/Linux/BSD имеет ограничение на количество 
байтов, которые можно использовать для аргумента командной строки и переменных среды.
Максимальное количество можно узнать командой 
```bash
vagrant@vagrant:~$ getconf ARG_MAX
2097152
```

11. `[[ -d /tmp ]]` проверяет наличие файла и то, что он является каталогом "True if file exists and is a directory."
12. Добемся в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:

     ```bash
     bash is /tmp/new_path_directory/bash
     bash is /usr/local/bin/bash
     bash is /bin/bash
     ```
```bash    
vagrant@vagrant:~$ mkdir /tmp/new_path_directory
vagrant@vagrant:~$ cp /bin/bash /tmp/new_path_directory
vagrant@vagrant:~$ PATH=/tmp/new_path_directory:$PATH
vagrant@vagrant:~$ type -a bash
bash is /tmp/new_path_directory/bash
bash is /usr/bin/bash
bash is /bin/bash
```
     

13. C помощью at можно запланировать выполнение команды в указанное время, а с помощью batch во время, когда ресурсы машины свободны

