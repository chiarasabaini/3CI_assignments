TITLE

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA

; definizione segmento di codice
.CODE
start:
        MOV AX, @DATA       ; inizializzazione registro
        MOV DS, AX          ; di segmento DS
        
        JMP read

read:
        MOV AH, 07h         ; lettura senza scrittura a video
        INT 21h

        CMP AL, 0Dh         ; check if carattere == carattere
        JZ  end

        MOV AH, 02h         ; scrittura "*" instead del carattere premuto
        MOV DL, 2Ah
        INT 21h

        JMP read

end:

        MOV AH, 4Ch         ; ritorno al sistema operativo
        INT 21h
        
; eventuali procedure

        END     start