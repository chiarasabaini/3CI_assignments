TITLE

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
password db 32 dup(?), 0

; definizione segmento di codice
.CODE
start:
        MOV AX, @DATA       ; inizializzazione registro
        MOV DS, AX          ; di segmento DS
        
        CALL    pwd


myend:
        MOV AH, 4Ch         ; ritorno al sistema operativo
        INT 21h
        
; eventuali procedure
pwd proc
        read:
                MOV AH, 07h         ; lettura senza scrittura a video (echo off)
                INT 21h

                CMP AL, 0Dh         ; check if char == invio
                JZ  my_end

                MOV AH, 02h         ; scrittura "*" invece del carattere premuto
                MOV DL, 2Ah
                INT 21h

                JMP read
        
        my_end:
                RET
pwd endp

        END     start