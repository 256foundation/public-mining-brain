# bitaxeorg/ESP-Miner issue #99: Проблемы получения заданий от пула

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/99
> Collected: 2026-10-07
> Published: 2024-01-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 99
- State: closed
- Author: pinokio240
- Opened: 2024-01-29
- Closed: 2024-03-15
- Labels: none

## Description

Майнер  JDHX Bit lattery BM1397 v3.8 z
Не работает с пулом nicehash.com, zpool.ca :
"₿ (599607) stratum_task: abandoning work
₿ (599607) create_jobs_task: New Work Dequeued beac
₿ (601597) stratum_task: rx"
 Можете реализовать их поддержку? 
Так же предлагаю подключение к пулам сделать одной строкой  как в консольных майнерах  для ПК. Например в CGMiner  cgminer --scrypt -o stratum+tcp://east1.us.stratum.dedicatedpool.com:3351 -u user.1 -p x , где можно например не указывать пароль или добавить флажок чтоб его не использовать 
 
Будет ли поддержка с методом  вознаграждения пула:  PPS, PPLNS, PPS+, SMPPS. 

 Наблюдается еще ошибка после обновления до [v2.0.7](https://github.com/skot/ESP-Miner/releases/tag/v2.0.7). После изменения настроек начинается частое переподключение к WI-FI сети и на домашней странице  то появляется то пропадает " Danger: Low voltage"  
 Пожалуйста укажите что понизить версию прошивки не получится без программатора. Иначе будет "кирпич" 

## Comments

### n0rthranger on 2024-01-29

Had the same issue with the Danger: Low Voltage 

https://damus.io/note10w92ncx6xxscsj4384xr3gkgtk0j7zcjrpw0kcp7anltfesmv5yq5dpph6

### benjamin-wilson on 2024-03-15

Low voltage is power supply issues, other comments not planned.
