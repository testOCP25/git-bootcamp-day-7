# Содержание
- [Содержание](#содержание)
- [LAB — день 7](#lab--день-7)
  - [Базовая задача — `01-platforms-tour`](#базовая-задача--01-platforms-tour)
    - [Ссылки на репозитории](#ссылки-на-репозитории)
    - [GitLab — скриншоты (3)](#gitlab--скриншоты-3)
    - [GitFlic — скриншоты (3)](#gitflic--скриншоты-3)
    - [GitVerse — скриншоты (3)](#gitverse--скриншоты-3)
    - [Таблица сравнения платформ](#таблица-сравнения-платформ)
    - [Команды](#команды)
    - [Впечатления (2–3 предложения)](#впечатления-23-предложения)
  - [⭐1 — bare headless](#1--bare-headless)
  - [⭐2 — Gitea](#2--gitea)
  - [⭐3 — GitLab CE self-hosted](#3--gitlab-ce-self-hosted)


# LAB — день 7

## Базовая задача — `01-platforms-tour`

### Ссылки на репозитории

| Платформа | URL |
|-----------|-----|
| GitHub (основной) | https://github.com/testOCP25/git-bootcamp-day-7 |
| GitLab | https://gitlab.com/testOCP25/git-bootcamp-day-7 |
| GitFlic | https://gitflic.ru/project/rogger/git-bootcamp-day-7 |
| GitVerse | https://gitverse.ru/rogger/git-bootcamp-day-7 |

### GitLab — скриншоты (3)

1. SSH-ключ в UI:

![GitLab SSH keys](screenshots/gitlab-ssh-keys.png)

2. Терминал `ssh -T`:

![GitLab ssh -T](screenshots/gitlab-ssh-test.png)

3. Репозиторий после push (ветки + тег):

![GitLab repository](screenshots/gitlab-repo.png)

### GitFlic — скриншоты (3)

1. SSH-ключ в UI:

![GitFlic SSH keys](screenshots/gitflic-ssh-keys.png)

2. Терминал `ssh -T`:

![GitFlic ssh -T](screenshots/gitflic-ssh-test.png)

3. Репозиторий после push:

![GitFlic repository](screenshots/gitflic-repo.png)

### GitVerse — скриншоты (3)

1. SSH-ключ в UI:

![GitVerse SSH keys](screenshots/gitverse-ssh-keys.png)

2. Терминал `ssh -T`:

![GitVerse ssh -T](screenshots/gitverse-ssh-test.png)

3. Репозиторий после push:

![GitVerse repository](screenshots/gitverse-repo.png)

### Таблица сравнения платформ

| Возможность | GitHub | GitLab | GitFlic | GitVerse |
|-------------|--------|--------|---------|----------|
| SSH-ключ через UI | да | да | да | да |
| Markdown render в README | да | да | да | да |
| Issues встроены | да | да | да | да |
| PR / Merge Request | PR | MR | MR | MR |
| Встроенный CI | Actions | GitLab CI/CD | есть, встроенный CI/CD | GitVerse Actions (CI/CD)  |
| Релизы / теги в UI | да | да | да | да |
| Видимость для незалогиненных | да | да | да | да |
| Что-то особенное | Copilot, Actions, огромное сообщество | единая DevOps-платформа (All-in-One) | SAST/DAST/SCA, реестр пакетов, российская юрисдикция | GigaCode (ИИ-ассистент), GigaIDE (облачная среда) |



### Команды

```bash
# git remote add gitlab ...
# git remote add gitflic ...
# git remote add gitverse ...
# git push ... --tags
# ssh -T git@gitlab.com
# ssh -T git@gitflic.ru
# ssh -T git@gitverse.ru

git remote add gitlab git@gitlab.com:testOCP25/git-bootcamp-day-7.git
git remote add gitflic git@gitflic.ru:rogger/git-bootcamp-day-7.git
git remote add gitverse git@gitverse.ru:rogger/git-bootcamp-day-7.git

git push gitlab  --tags
git push gitlab  --all
git push gitflic --all
git push gitflic --tags
git push gitverse --all
git push gitverse --tags

ssh -T git@gitlab.com
ssh -T git@gitflic.ru
ssh -T git@gitverse.ru
```

### Впечатления (2–3 предложения)

Удвило, что у нас есть несколько проектов, которые похожи на Git. На любой вкус и цвет) Но при этом странно, что забыли https://sourcecraft.dev/. Я его себе тоже добавил, проверил, работает нормально. Понятно, что для того, чтобы нормально осознать плюсы и минусы каждой платформы, надо какое-то время поработать с каждой.

---

## ⭐1 — bare headless

**Где bare на VM и URL remote `vm`:**

Для задачки пришлось поковыряться - в дефолтной конгфиге заводиться не захотел, сначала поменял образ, но это не помогло, в итоге остановился на влкючении GUI (подвисал на создании ключей) и выделении 1Гб памяти.

**Файл vagrant:**
```text
#ENV['VAGRANT_SERVER_URL'] = 'https://vagrant.elab.pro'

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"
  config.vm.box_version = "202510.26.0" # add
#  config.vm.box = "net9/ubuntu-24.04-arm64"
  config.vm.box_check_update = false
  config.vm.hostname = "bare-git-host"

  config.vm.network "private_network", ip: "192.168.56.10"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider "virtualbox" do |vb|
    vb.name = "git-bootcamp-bare"
    vb.memory = "1024"     # change
    vb.cpus = 1
    vb.gui = true          # change
  end

  config.vm.provision "shell", path: "provision.sh"
end
```

![push в bare](screenshots/star1-push.png)

![git log после clone](screenshots/star1-clone-log.png)

---

## ⭐2 — Gitea

GitLab — тяжёлая DevOps-платформа «всё в одном», требующая много ресурсов, но предлагающая встроенный CI/CD, Container Registry, сканирование безопасности и мониторинг. Gitea — легковесный аналог на Go, работающий даже на Raspberry Pi, предоставляющий базовый набор (репозитории, Issues, PR, Actions), но без тяжёлых встроенных инструментов DevOps. Выбирайте GitLab для больших команд с потребностью в единой платформе, а Gitea — для небольших проектов, хобби или когда ресурсы сервера сильно ограничены.

![Gitea repository](screenshots/star2-gitea-repo.png)

![Gitea pull request](screenshots/star2-gitea-pr.png)

---

## ⭐3 — GitLab CE self-hosted

**GitLab CE vs Gitea: RAM, время старта (2–3 предложения):**

[FIXME]

![GitLab project](screenshots/star3-gitlab-project.png)

![GitLab merge request](screenshots/star3-gitlab-mr.png)
