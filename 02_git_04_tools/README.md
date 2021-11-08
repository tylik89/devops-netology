# Домашнее задание к занятию «2.4. Инструменты Git»

Для выполнения заданий в этом разделе склонируем репозиторий с исходным кодом 
терраформа https://github.com/hashicorp/terraform 
```bash
$ git clone git@github.com:hashicorp/terraform.git
```

###1. Найдем полный хеш и комментарий коммита, хеш которого начинается на `aefea`.
 
Простой метод найти полный хеш и комментарий  воспользоваться [git show](https://git-scm.com/docs/git-show)
c параметром --pretty=oneline. Флаг -s уберет вывод diff
```bash
$ git show --pretty=oneline -s aefea
aefead2207ef7e2aa5dc81a34aedf0cad4c32545 Update CHANGELOG.md
```
также можно использовать format:<string> 
```bash
git show --pretty="Полный хеш комита начинающего на aefea  %H %nКоминтарий коммита: %s" -s aefea
Полный хеш комита начинающего на aefea  aefead2207ef7e2aa5dc81a34aedf0cad4c32545 
Коминтарий комита: Update CHANGELOG.md
```
2. Найдем какому тегу соответствует коммит `85024d3`
```bash
$ git tag  --points-at 85024d3
v0.12.23
```
```bash
$ git show --oneline -s 85024d3
85024d310 (tag: v0.12.23) v0.12.23
```

3. Найдем сколько родителей у коммита `b8d720`  и выведим их хеши.
```bash
$ git show --pretty="Полный хеш родителей  %P " -s b8d720
Полный хеш родителей  56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b 
```
4. Перечислим хеши и комментарии всех коммитов которые были сделаны между тегами  v0.12.23 и v0.12.24.
```bash
$ git log --pretty=oneline  v0.12.24...v0.12.23
33ff1c03bb960b332be3af2e333462dde88b279e (tag: v0.12.24) v0.12.24
b14b74c4939dcab573326f4e3ee2a62e23e12f89 [Website] vmc provider links
3f235065b9347a758efadc92295b540ee0a5e26e Update CHANGELOG.md
6ae64e247b332925b872447e9ce869657281c2bf registry: Fix panic when server is unreachable
5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 website: Remove links to the getting started guide's old location   '
06275647e2b53d97d4f0a19a0fec11f6d69820b5 Update CHANGELOG.md
d5f9411f5108260320064349b757f55c09bc4b80 command: Fix bug when using terraform login on Windows
4b6d06cc5dcb78af637bbb19c198faff37a066ed Update CHANGELOG.md
dd01a35078f040ca984cdd349f18d0b67e486c35 Update CHANGELOG.md
225466bc3e5f35baa5d07197bbc079345b77525e Cleanup after v0.12.23 release
```
5. Найдем коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит 
так `func providerSource(...)` (вместо троеточего перечислены аргументы).
```bash
git log -S'func providerSource(' --pretty=oneline  
8c928e83589d90a031f811fae52a81be7153e82f main: Consult local directories as potential mirrors of providers
```

6. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.
Для поиска изменний тела фукции сначала найдем файл где определена функция 
```bash
$ git grep "globalPluginDirs"
commands.go:            GlobalPluginDirs: globalPluginDirs(),
commands.go:    helperPlugins := pluginDiscovery.FindPlugins("credentials", globalPluginDirs())
internal/command/cliconfig/config_unix.go:              // FIXME: homeDir gets called from globalPluginDirs during init, before
plugins.go:// globalPluginDirs returns directories that should be searched for
plugins.go:func globalPluginDirs() []string { # определения функции 
```

```bash
$ git log -s -L '/globalPluginDirs/',/^}/:plugins.go --pretty=oneline
78b12205587fe839f10d946ea3fdc06719decb05 Remove config.go and update things using its aliases
52dbf94834cb970b510f2fba853a5b49ad9b1a46 keep .terraform.d/plugins for discovery
41ab0aef7a0fe030e84018973a64135b11abcd70 Add missing OS_ARCH dir to global plugin paths
66ebff90cdfaa6938f26f908c7ebad8d547fea17 move some more plugin search path logic to command
8364383c359a6b738a436d1b7745ccdce178df47 Push plugin discovery down into command package
```
7. Найдем кто автор функции `synchronizedWriters`? 
```bash
git log -S "synchronizedWriters" --oneline --pretty="%H автор  %an" 
bdfea50cc85161dea41be0fe3381fd98731ff786 автор  James Bardin
fd4f7eb0b935e5a838810564fd549afe710ae19a автор  James Bardin
5ac311e2a91e381e2f52234668b49ba670aa0fe5 автор  Martin Atkins
```
5ac311e2a91e381e2f52234668b49ba670aa0fe5 автор  Martin Atkins
---

