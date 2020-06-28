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
        MOV BL, 31h
        MOV [a], BL
        INC [a]
        MOV DL, [a]
        MOV AL, 1
        MOV [a], AL
        INC [a]
        MOV DL, [a]
        MOV AH, 02h
        INT 21h

        MOV AH, 4Ch         ; ritorno al sistema operativo
        INT 21h

; eventuali procedure

        END     start