TITLE

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
a   db  ?

; definizione segmento di codice
.CODE
start:
        MOV AX, @DATA       ; inizializzazione registro
        MOV DS, AX          ; di segmento DS

        MOV DL, 30h         ; inizializzazione contatore DL (30h == 0)
        MOV AH, 02h         ; print(?)

inizio:
        CMP DL, 3Ah         ; test

        JE uscita           ; jump a uscita

        INT 21h             ; print(vedi riga 20?)
        INC DL

        MOV DH, DL          ; salvo la cifra

        MOV DL, 3Bh         ; carico il ";"
        INT 21h             ; printa ";"

        MOV DL, 20h         ; carico " "
        INT 21h             

        MOV DL, 0Ah         ; carico LF: line feed (va a capo)
        INT 21h

        MOV DL, DH          ; ripristino DL

        JMP inizio          ; salto incondizionato all'inizio

        MOV AH, 4Ch         ; ritorno al sistema operativo
        INT 21h

; eventuali procedure

        END     start