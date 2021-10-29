# Домашнее задание к занятию «2.1. Системы контроля версий.» - Алексей Тылик 

Файл в катологе Terraform [.gitignor](Terraform/.gitignore) позваляет исключить 
локальные катологи `.terraform`,
файлы  `.tfstate `,
Крэш логи  `crash.log`,
все файлы `.tfvars`, которые могут содержать конфиденциальные данные, такие как пароль, секретные ключи и другие секреты.

Игнорировать файлы переопределения `override.tf override.tf.json *_override.tf *_override.tf.json`,
файлы конфигурации командной строки `.terraformrc terraform.rc`
new line