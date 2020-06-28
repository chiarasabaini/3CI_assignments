TITLE

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
password db 'Buon San Valentino!', 0

; definizione segmento di codice
.CODE
start:
        MOV AX, @DATA       ; inizializzazione registro
        MOV DS, AX          ; di segmento DS
        
        LEA BX, password
        PUSH BX

        CALL    cript
        MOV SI, [BP + 4]

myend:
        MOV AH, 4Ch         ; ritorno al sistema operativo
        INT 21h
        
; eventuali procedure
cript proc
        PUSH BP
        MOV BP, SP

        MOV AH, 02
        MOV CX, 0h
        
        inizio:  
                MOV AH, 07h         ; lettura senza scrittura a video (echo off)
                INT 21h

                CMP AL, 0Dh         ; check if char == invio
                JZ  my_end

                MOV [BX], AL        ; memorizzazione password

                ADD AL, 2

                MOV AH, 02h         ;
                MOV DL, AL
                INT 21h

                INC CX
                JMP inizio          ; salto incondizionato all'inizio

        my_end:
                MOV SP, BP
                POP BP
                RET
cript endp

        END     start