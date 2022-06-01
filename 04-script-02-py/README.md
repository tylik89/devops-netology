# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательные задания

1. Есть скрипт:
	```python
    #!/usr/bin/env python3
	a = 1
	b = '2'
	c = a + b
	```
	
| Вопрос  | Ответ                                                                             |
| ------ |----------------------------------------------------------------------|
| Какое значение будет присвоено переменной `c`?  | значение не может быть присвоено, т.к. переменные разных типов (integer и string)<br/>`>>> a=1; b='2'; c=a+b`<br/>`Traceback (most recent call last):`<br/>`  File "<stdin>", line 1, in <module>`<br/>`TypeError: unsupported operand type(s) for +: 'int' and 'str'`<br/>  |
| Как получить для переменной `c` значение 12?  | `c = str(a) + b` (преобразовать переменную `a` в string)                       |
| Как получить для переменной `c` значение 3?  | `c = a + int(b)` (преобразовать переменную `b` в integer)                   |


2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

	```python
    #!/usr/bin/env python3
    import os
	bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
	result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False
	for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
            break
	```
Модифицированный скрипт:
```python
import os

dir_git = "~/web/devops-netology"
bash_command = ["cd "+dir_git, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:      ', f'{dir_git}/')
        print(prepare_result)
```
Вывод скрипта :
```shell
/usr/bin/python3.10 /home/a1/web/devops-netology/04-script-02-py/script_00.py
~/web/devops-netology/01_intro_01/README.md
~/web/devops-netology/README.md

Process finished with exit code 0
```

3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

скрипт:
```python
import os
import sys


try:
    if os.path.exists(sys.argv[1]):
        dir_git = sys.argv[1]
    else:
        sys.exit(f'{sys.argv[1]}-это не директория')
except IndexError:
    dir_git = "~/web/devops-netology"

bash_command = ["cd "+dir_git, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:      ', f'{dir_git}/')
        print(prepare_result)
```
Вывод скрипта :
```shell
a1@a1:~/web/devops-netology/04-script-02-py$ python3 script_01.py 
~/web/devops-netology/01_intro_01/README.md
~/web/devops-netology/03-sysadmin-09-security/README.md
~/web/devops-netology/04-script-02-py/README.md
~/web/devops-netology/README.md
a1@a1:~/web/devops-netology/04-script-02-py$ python3 script_01.py 6
6-это не директория
a1@a1:~/web/devops-netology/04-script-02-py$ python3 script_01.py ~
fatal: не найден git репозиторий (или один из родительских каталогов): .git
a1@a1:~/web/devops-netology/04-script-02-py$ python3 script_01.py ~/web/sysadm-homeworks
/home/a1/web/sysadm-homeworks/03-sysadmin-06-net/README.md
/home/a1/web/sysadm-homeworks/README.md

```

4. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.

скрипт:
```python
import socket


hosts = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
count = 3
while count > 0:
    print(f'\n---------------Новая проверка---------------\n')
    for host, ip in hosts.items():
        new_ip = socket.gethostbyname(host)
        print(f"{host} - {new_ip}")

        if (ip != new_ip):
            print (f'[ERROR] {host} IP mismatch: {ip} {new_ip}')
            hosts[host]=new_ip

    count -= 1
```
Вывод скрипта :
```shell
/usr/bin/python3.10 /home/a1/web/devops-netology/04-script-02-py/script_02.py

---------------Новая проверка---------------

drive.google.com - 74.125.131.194
[ERROR] drive.google.com IP mismatch: 0.0.0.0 74.125.131.194
mail.google.com - 108.177.14.83
[ERROR] mail.google.com IP mismatch: 0.0.0.0 108.177.14.83
google.com - 173.194.73.138
[ERROR] google.com IP mismatch: 0.0.0.0 173.194.73.138

---------------Новая проверка---------------

drive.google.com - 74.125.131.194
mail.google.com - 108.177.14.19
[ERROR] mail.google.com IP mismatch: 108.177.14.83 108.177.14.19
google.com - 173.194.73.138

---------------Новая проверка---------------

drive.google.com - 74.125.131.194
mail.google.com - 108.177.14.19
google.com - 173.194.73.138

Process finished with exit code 0

```

