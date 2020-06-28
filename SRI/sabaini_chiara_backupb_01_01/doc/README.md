# BACKUPB
---

## Description
Da Wikipedia:

*"Con backup nella sicurezza informatica si indica il processo atto a ottenere una o più copie di riserva dei dati, da utilizzare in caso di eventi malevoli accidentali o intenzionali. Si tratta dunque di un procedimento di sicurezza delle informazioni, in particolare di disaster recovery nonché di ridondanza fisica dei dati. "*

Repository

Qualsiasi strategia di backup inizia con un concetto di un repository di dati. I dati dei backup devono essere essere organizzati (schema di backup) per gradi e memorizzati semplicemente anche su un foglio di carta con una lista di tutti i supporti di backup (CD, ecc) e le date sono stati prodotti. Una configurazione più sofisticata potrebbe includere un indice computerizzato, catalogo, o un database relazionale. Diversi approcci hanno diversi vantaggi. Parte del modello è lo schema di rotazione di backup.

Non strutturato

Un repository non strutturato può essere semplicemente una pila di o CD-R o DVD-R con informazioni minime su ciò che è stato eseguito il backup e quando. Questo è il più semplice da attuare, ma ha poche probabilità di ottenere un elevato livello di recupero dei dati in quanto manca automazione (orchestrazione).

Completo

Un repository di questo tipo contiene immagini di sistema complete prese in uno o più specifici momenti nel tempo. Questa tecnologia è spesso utilizzato dai tecnici informatici per salvare un sistema configurato e perfettamente funzionante, quindi è generalmente più utile per la distribuzione di una configurazione standard per molti sistemi, piuttosto che come uno strumento per fare copie di backup in corso di sistemi diversi.

---
## Oggetto

Si vuole permette il backup completo di una cartella con relative eventuali sotto cartelle

---

**Backup completo**

Il backup della cartella sorgente viene effettuato completamente su una nuova cartella

---
## Implementazione del backup

Per la realizzazione del backup (di questa esperienza) si utilizza il programma XCOPY

---
### Comando XCOPY

Il comando XCOPY permette la copia di file e di cartelle. La sintassi (breve) è la seguente:

XCOPY somefolder backupfolder /E /C /I /Y

where:

/E copia folder e subfolder anche vuoti
/C continua a copiare anche in seguito a errori
/I se la destinazione non esiste e copia più file assume che la destinazione sia un folder
/Y sopprime la richiesta di confermare la sovrascrittura

---
#### Esempio:

XCOPY somefolder backupfolder /E /C /I /Y

---
#### Exit codes for Xcopy

Molti comandi fornisco, in output, codici che segnalano lo stato del comando dopo la sua
esecuzione.
I codici di uscita di XCOPY sono i seguenti:

Exit code Description

0 Files were copied without error.

1 No files were found to copy.

2 The user pressed Ctrl+C to terminate xcopy.

4 Various errors including insufficient memory or disk space, an invalid drive name, or invalid syntax.

5 Disk write error occurred.

---
## Changelog 
- [01.01_2019-12-17](#0101_2019-12-17)

---
### 01.01_2019-12-17
 - #### Added
	 - Does a backup of the Documents folder in C:\Temp



---
By Davide Castellani & Sabaini Chiara
---
If you have any problem please contact us:
- davidecastellani@castellanidavide.it
- chiara@sabaini.com
