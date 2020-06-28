TITLE  

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
msg   db ?

; definizione segmento codice
.CODE
start:
        mov   ax, @DATA             ; inizializzazione registro
        mov   ds, ax                ; di segmento DS
        
        mov ax, "Ok"                ; inizializzazione parametri
        push ax
        mov ax, 2101h
        push ax

        CALL f

        mov ah, 4ch                 ; ritorno al sistema operativo
        int 21h

; eventuali procedure

f proc
    push bp
    mov bp, sp
    add sp, -2                      ; 2 byte local var

    ;print ok
    mov ax, 02h

    mov dl, [bp + 7]                ;primo parametro
    int 21h

    mov dl, [bp + 6]                ;secondo parametro
    int 21h

    mov dl, [bp + 5]                ;terzo parametro
    int 21h

    mov dl, [bp + 4]                ;quarto parametro
    int 21h

    mov dl, 10                      ;new line
    int 21h

    mov sp, bp
    pop bp
    ret 4                           ;4 byte di parametri

f endp

    END   start
