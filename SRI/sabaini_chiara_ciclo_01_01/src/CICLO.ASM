;CICLO

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
i   dw  65530

; definizione segmento codice
.CODE
start:
       mov   ax, @DATA             ; inizializzazione registro
       mov   ds, ax                ; di segmento DS

       MOV AX, [i]
       INC AX

       mov ah, 4ch                 ; ritorno al sistema operativo
       int 21h

; eventuali procedure
       
       END   start

