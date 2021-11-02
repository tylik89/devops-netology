# Домашнее задание к занятию «2.3. Ветвления в Git»

Давайте потренеруемся делать merge и rebase, чтобы понять разницу и научиться решать конфликты.

## Задание №1 – Ветвление, merge и rebase. 

1.Создадим в своем репозитории каталог `02_git_03_branching` и в нем два файла `merge.sh` и `rebase.sh` с 
содержимым:
```bash
#!/bin/bash
# display command line options

count=1
for param in "$*"; do
    echo "\$* Parameter #$count = $param"
    count=$(( $count + 1 ))
done
```

```bash
$ mkdir 02_git_03_branching
$ cat >02_git_03_branching/merge.sh <<EOF
#!/bin/bash

# display command line options

count=1
for param in "\$*"; do
    echo "\\\$* Parameter #\$count = \$param"
    count=\$(( \$count + 1 ))
done
EOF
$ cp 02_git_03_branching/merge.sh 02_git_03_branching/rebase.sh
```
2. Создадим коммит с описанием `prepare for merge and rebase` и отправим его в ветку main. 
```bash
$ git add 02_git_03_branching/merge.sh 02_git_03_branching/rebase.sh
$ git commit -m "prepare for merge and rebase"
```
#### Подготовка файла merge.sh.
1. Создадим ветку `git-merge`. 
```bash
$ git branch git-merge && git checkout git-merge || git checkout -b git-merge 
```
2. Заменим в ней содержимое файла `merge.sh` на
```bash
#!/bin/bash
# display command line options

count=1
for param in "$@"; do
    echo "\$@ Parameter #$count = $param"
    count=$(( $count + 1 ))
done
```


```bash
$ sed -i 's/\*/@/' 02_git_03_branching/merge.sh
```
3. Создадим коммит `merge: @ instead *` отправьте изменения в репозиторий.
```bash
$ git add 02_git_03_branching/merge.sh
$ git commit -m " merge: @ instead *"
$ git push origin git-merge
```
4. внесем еще одно изменение в `merge.sh` 
```bash
#!/bin/bash
# display command line options

count=1
while [[ -n "$1" ]]; do
    echo "Parameter #$count = $1"
    count=$(( $count + 1 ))
    shift
done
```

```bash
$ cat >02_git_03_branching/merge.sh <<EOF
#!/bin/bash
# display command line options

count=1
while [[-n "\$1"]]; do
    echo "Parameter #\$count = \$1"
    count=\$(( \$count + 1 ))
    shift
done
EOF
```
Теперь скрипт будет отображать каждый переданный ему параметр отдельно. 

5. Создадим коммит `merge: use shift` и отправьте изменения в репозиторий. 
```bash
$ git add 02_git_03_branching/merge.sh
$ git commit -m " merge: use shift"
$ git push origin git-merge
```
#### Изменим main.
1. Вернитесь в ветку `main`. 
```bash
$ git checkout main
```
2. Предположим, что кто-то, пока мы работали над веткой `git-merge`, изменил `main`. Для этого
изменим содержимое файла `rebase.sh` на следующее
```bash
#!/bin/bash
# display command line options

count=1
for param in "$@"; do
    echo "\$@ Parameter #$count = $param"
    count=$(( $count + 1 ))
done

echo "====="
```
В этом случае скрипт тоже будет отображать каждый параметр в новой строке. 
```bash
$ cat >02_git_03_branching/rebase.sh <<EOF
#!/bin/bash
# display command line options

count=1
for param in "\$@"; do
    echo "\\\$@ Parameter #\$count = \$param"
    count=\$(( \$count + 1 ))
done

echo "====="
EOF
```
3. Отправляем измененную ветку `main` в репозиторий.
```bash
$ git commit -am " rebase: @ instead * and add echo==="
$ git push origin main
```

#### Подготовка файла rebase.sh.
1. Предположим, что теперь другой участник нашей команды 
не сделал `git pull`, либо просто хотел ответвиться не от 
последнего коммита в `main`, а от коммита когда мы только создали два файла
`merge.sh` и `rebase.sh` на первом шаге.  
Для этого при помощи команды `git log` найдем хэш коммита `prepare for merge and rebase` 
и выполним `git checkout` на него примерно так:
`git checkout 8baf217e80ef17ff577883fda90f6487f67bbcea` (хэш будет другой).
2. Создадим ветку `git-rebase` основываясь на текущем коммите. 
```bash
$ git checkout -b git-rebase 
```
3. И изменим содержимое файла `rebase.sh` на следующее, тоже починив скрипт, 
но немного в другом стиле
```bash
#!/bin/bash
# display command line options

count=1
for param in "$@"; do
    echo "Parameter: $param"
    count=$(( $count + 1 ))
done

echo "====="
```
```bash
$ cat >02_git_03_branching/rebase.sh <<EOF
#!/bin/bash
# display command line options

count=1
for param in "\$@"; do
    echo "Parameter: \$param"
    count=\$(( \$count + 1 ))
done

echo "====="
EOF
```
4. Отправим эти изменения в ветку `git-rebase`, с комментарием `git-rebase 1`.
```bash
$ git commit -am "git-rebase 1"
```
5. И сделаем еще один коммит `git-rebase 2` с пушем заменив `echo "Parameter: $param"` 
на `echo "Next parameter: $param"`.
```bash
$ sed -i 's/echo "Parameter: \$param"/echo "Next parameter: \$param"/' 02_git_03_branching/rebase.sh
$ git commit -am "git-rebase 2"
$ git push origin git-rebase
```
#### Промежуточный итог. 
Мы сэмулировали типичную ситуации в разработке кода, когда команда разработчиков 
работала над одним и тем же участком кода, причем кто-то из разработчиков 
предпочитаем делать `merge`, а кто-то `rebase`. Конфилкты с merge обычно решаются достаточно просто, 
а с rebase бывают сложности, поэтому давайте смержим все наработки в `main` и разрешим конфликты. 

Посмотрим что получилось  на странице `network` в гитхабе, находящейся по адресу 
`https://github.com/tylik89/devops-netology/network`:
![Созданы обе ветки](img/01.png)

#### Merge
Сливаем ветку `git-merge` в main и отправляем изменения в репозиторий, должно получиться без конфликтов:
```bash
$ git merge git-merge
$ git push origin main
```  
В результате получаем такую схему:
![Первый мерж](img/02.png)

#### Rebase
1. А перед мержем ветки `git-rebase` выполним ее `rebase` на main. Да, мы специально создали
ситуацию с конфликтами, чтобы потренироваться их решать. 
2. Переключаемся на ветку `git-rebase` и выполняем `git rebase -i main`. 
В открывшемся диалоге должно быть два выполненных нами коммита, давайте заодно объединим их в один, 
указав слева от нижнего `fixup`. 
В результате получаем что-то подобное:

```bash
$ git checkout git-rebase
$ git rebase -i main
Автослияние 02_git_03_branching/rebase.sh
КОНФЛИКТ (содержимое): Конфликт слияния в 02_git_03_branching/rebase.sh
error: не удалось применить коммит 3b02b63… git-rebase 1
Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 3b02b63... git-rebase 1

``` 
Если посмотреть содержимое файла `rebase.sh`, то увидим метки, оставленные гитом для решения конфликта:
```bash
#!/bin/bash
# display command line options

count=1
for param in "$@"; do
<<<<<<< HEAD
    echo "\$@ Parameter #$count = $param"
=======
    echo "Parameter: $param"
>>>>>>> 3b02b63... git-rebase 1
    count=$(( $count + 1 ))
done

echo "====="
```
Удалим метки, отдав предпочтение варианту
```bash
echo "\$@ Parameter #$count = $param"
```
сообщим гиту, что конфликт решен `git add rebase.sh` и продолжим ребейз `git rebase --continue`.
```bash
$ git add 02_git_03_branching/rebase.sh
$ git rebase --continue
```

И опять в получим конфликт в файле `rebase.sh` при попытке применения нашего второго коммита. 
Давайте разрешим конфликт, оставив строчку `echo "Next parameter: $param"`.

Далее опять сообщаем гиту о том, что конфликт разрешен `git add rebase.sh` и продолжим ребейз `git rebase --continue`.
В результате будет открыт текстовый редактор предлагающий написать комментарий к новому объединенному коммиту:
```
# This is a combination of 2 commits.
# This is the 1st commit message:

Merge branch 'git-merge'

# The commit message #2 will be skipped:

# git 2.3 rebase @ instead * (2)
```
Все строчки начинающиеся на `#` будут проигнорированны. 

После сохранения изменения, гит сообщит
```
Successfully rebased and updated refs/heads/git-rebase
```
И попробуем выполнить `git push`, либо `git push -u origin git-rebase` чтобы точно указать что и куда мы хотим запушить. 
Эта команда завершится с ошибкой:
```bash
git push
To github.com:andrey-borue/devops-netology.git
 ! [rejected]        git-rebase -> git-rebase (non-fast-forward)
error: failed to push some refs to 'git@github.com:andrey-borue/devops-netology.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
Это произошло, потому что мы пытаемся перезаписать историю. 
Чтобы гит позволил нам это сделать, давайте добавим флаг `force`:
```bash
git push -u origin git-rebase -f
Enumerating objects: 10, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 443 bytes | 443.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:andrey-borue/devops-netology.git
 + 1829df1...e3b942b git-rebase -> git-rebase (forced update)
Branch 'git-rebase' set up to track remote branch 'git-rebase' from 'origin'.
```

Теперь можно смержить ветку `git-rebase` в main без конфликтов и без дополнительного мерж-комита простой перемоткой. 
```
$ git checkout main
Переключено на ветку «main»
Ваша ветка обновлена в соответствии с «origin/main».


$ git merge git-rebase
Updating 6158b76..45893d1
Fast-forward
 branching/rebase.sh | 3 +--
 1 file changed, 1 insertion(+), 2 deletions(-)
```

Цель задания - попробовать на практике то, как выглядит решение конфликтов.
Обычно при нормальном ходе разработки выполнять `rebase` достаточно просто, 
что позволяет объединить множество промежуточных коммитов при решении задачи, чтобы 
не засорять историю, поэтому многие команды и разработчики предпочитают такой способ.   


Есть еще такой тренажер https://learngitbranching.js.org/, где можно потренироваться в работе с 
деревом коммитов и ветвлений. 

