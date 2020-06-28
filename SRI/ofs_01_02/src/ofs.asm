TITLE

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
msg   db "Hello, world!", 0h

; definizione segmento codice
.CODE
start:
        MOV   AX, @DATA             ; inizializzazione registro
        MOV   DS, ax                ; di segmento DS
        
        LEA   BX, msg               ; riferimento a msg
        
        PUSH BX                     ; variabile locale
        
        CALL vis

        MOV AH, 4ch                 ; ritorno al sistema operativo
        INT 21h

; eventuali procedure

vis proc
        PUSH bp
        MOV bp, sp

        MOV BX, [BP + 4]

        MOV AH, 02h                 ; inizializzazione registro AH per visualizzazione
    
    check:
        CMP BX, 0Dh
        JZ end

        MOV DL, [BX]
        INT 21h

        INC BX
        JMP check

    end:  
        MOV SP, BP
        POP BP
        RET 2

vis endp

    END   start
