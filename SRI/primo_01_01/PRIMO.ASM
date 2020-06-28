TITLE  

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
a    db ?

; definizione segmento codice
.CODE
start:
       mov   ax, @DATA             ; inizializzazione registro
       mov   ds, ax                ; di segmento DS

       mov ah, 31h
       mov [a], ah
       inc a
       mov dl, [a]
       mov ah, 02h
       int 21h

       mov ah, 1h
       mov [a], ah
       inc a
       mov dl, [a]
       mov ah, 02h
       int 21h

       mov ah, 4ch                 ; ritorno al sistema operativo
       int 21h

; eventuali procedure
       
       END   start

