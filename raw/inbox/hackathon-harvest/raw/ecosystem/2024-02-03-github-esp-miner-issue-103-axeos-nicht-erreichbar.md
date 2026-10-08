# bitaxeorg/ESP-Miner issue #103: AxeOS nicht erreichbar

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/103
> Collected: 2026-10-07
> Published: 2024-02-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 103
- State: closed
- Author: thekey82
- Opened: 2024-02-03
- Closed: 2024-03-15
- Labels: none

## Description

Nach ca 24-25h ist der Bitaxe nicht mehr über AxeOS erreichbar. Nach einem reboot funktioniert es dann wieder für 24-25h

## Comments

### jddebug on 2024-02-03

Ich hatte dieses Problem auch. Ich nahm den Kühlkörper ab, ersetzte die Wärmeleitpaste und setzte sie wieder zusammen. Danach waren meine Temperaturen viel niedriger und ich hatte nicht mehr das Problem, den Zugang zu verlieren.

### thekey82 on 2024-02-04

An der Temperatur liegt es definitiv nicht , diese liegt bei mir bei 36 Grad.

### monster4866 on 2024-02-04

> An der Temperatur liegt es definitiv nicht , diese liegt bei mir bei 36 Grad.

dann hast du v1, da ist der temperatursensor nicht richtig, 36c ist schon etwas hoch, ich habe ca. 30, schick mir mal ein screenshot von den ganzen daten auf der ersten seite links, clock, mv usw.

### thekey82 on 2024-02-04

![camphoto_342241519](https://github.com/skot/ESP-Miner/assets/74416112/a9840d82-a517-4927-af19-92f52c5f851f)

ich habe 2 Bitaxe. Exakt das selbe Problem bei beiden. 

### thekey82 on 2024-02-04

Es ist ein 201 Bord

### monster4866 on 2024-02-04

> ![camphoto_342241519](https://private-user-images.githubusercontent.com/74416112/302074687-a9840d82-a517-4927-af19-92f52c5f851f.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDcwMTcxMDEsIm5iZiI6MTcwNzAxNjgwMSwicGF0aCI6Ii83NDQxNjExMi8zMDIwNzQ2ODctYTk4NDBkODItYTUxNy00OTI3LWFmMTktOTJmNTJjNWY4NTFmLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjA0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIwNFQwMzIwMDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MmQyOTM5YjFlYWYzOGE2ZGViOWVjNDU4MWM2MGQ5ZjRlZDI2YzFhNDRhNDc5ZTA3MDFjY2U4OTc0NGNiYTQ1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.K4wYcyS2ymAJgfW6h04ZR1HW30D0iEP3MwT8G2k_omE)
> 
> ich habe 2 Bitaxe. Exakt das selbe Problem bei beiden.

wechsel erstmal das netzteil, sollte nie unter 5000mv fallen

https://amzn.eu/d/1stC5ll

201 ist v1, denke das problem hat sich mit dem neuen netzteil erledigt



### monster4866 on 2024-02-04

![IMG_9381](https://github.com/skot/ESP-Miner/assets/119421965/6ac6e635-d037-47cd-8655-2444665fb808)

so sieht das bei mir aus

### thekey82 on 2024-02-04

Okay danke ich werde es mal testen. Wie hoch ist die Temp dann in echt wenn die 36 Grad falsch sind?

### exobug on 2024-03-11

Habe das selbe Problem gelegentlich. Allerdings v204 hier. Vermutlich liegt es an der Temperatur, wenn ich die Taktrate höher setze. Seltsamerweise läuft das Hashing aber normal weiter.

### benjamin-wilson on 2024-03-15

Antwort auf den ursprünglichen Kommentar: Ich habe dieses Problem schon einmal gesehen. Es hängt mit etwas in Ihrem Netzwerk zusammen. Wird geschlossen, es sei denn, wir können das Problem reproduzieren.
