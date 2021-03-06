# Домашнее задание к занятию "4.1. Командная оболочка Bash: Практические навыки"

## Обязательная задача 1

Есть скрипт:
```bash
a=1
b=2
c=a+b
d=$a+$b
e=$(($a+$b))
```

Какие значения переменным c,d,e будут присвоены? Почему?

| Переменная  | Значение | Обоснование |
| ------------- |----------| ------------- |
| `c`  | `a+b`    | не было обращения к переменным, соответственно значение - символы после знака `=` |
| `d`  | `1+2`    | по умолчанию переменные строкового типа, поэтому  - значения переменных `a` и `b`, разделенные знаком `+` |
| `e`  | `3`      | т.к. явно  указали выполнение арифметической операции то резултат  сложение значений переменных `a` и `b` |


## Обязательная задача 2
На нашем локальном сервере упал сервис и мы написали скрипт, который постоянно проверяет его доступность, записывая дату проверок до тех пор, пока сервис не станет доступным (после чего скрипт должен завершиться). В скрипте допущена ошибка, из-за которой выполнение не может завершиться, при этом место на Жёстком Диске постоянно уменьшается. Что необходимо сделать, чтобы его исправить:
```bash
while ((1==1)
do
	curl https://localhost:4757
	if (($? != 0))
	then
		date >> curl.log
	fi
done
```
- в первой строке `while ((1==1)` нужно дописать скобку;
- нужно добавить `sleep` с указанием времени - для задания интервала проверки;
- нужно прописать условия выхода окончания цикла, например, добавив условие `else exit`.

### Ваш скрипт:
```bash
while (( 1 == 1 ))
  do
      curl https://localhost:4757
      if (($? != 0))
      then
          date >> curl.log
      else exit
      fi
      sleep 5
  done
```

## Обязательная задача 3
Необходимо написать скрипт, который проверяет доступность трёх IP: `192.168.0.1`, `173.194.222.113`, `87.250.250.242` по `80` порту и записывает результат в файл `log`. Проверять доступность необходимо пять раз для каждого узла.

### Ваш скрипт:
```bash
#!/usr/bin/bash
hosts=(192.168.0.1 173.194.222.113 87.250.250.242)

timeout=5
for i in {1..5}
do
date >> log
    for host in ${hosts[@]}
    do
        curl -Is --connect-timeout $timeout $host:80 >/dev/null
        echo "check" $host status=$? >> log
    done
done
  
```

## Обязательная задача 4
Необходимо дописать скрипт из предыдущего задания так, чтобы он выполнялся до тех пор, пока один из узлов не окажется недоступным. Если любой из узлов недоступен - IP этого узла пишется в файл error, скрипт прерывается.

### Ваш скрипт:
```bash
#!/usr/bin/bash
hosts=(192.168.0.1 173.194.222.113 87.250.250.242)
timeout=5
stat=0
while (($stat == 0))
do
    for host in ${hosts[@]}
    do
        curl -Is --connect-timeout $timeout $host:80 >/dev/null
        stat=$?
        if (($stat != 0))
        then
            echo  "$host\n" >> error
            exit
        fi
    done
done
```