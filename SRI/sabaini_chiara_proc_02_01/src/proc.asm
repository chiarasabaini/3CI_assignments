TITLE  

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
msg    db ?
; definizione segmento codice

.CODE
start:
    mov   ax, @DATA             ; inizializzazione registro
    mov   ds, ax                ; di segmento DS

    mov   ax, "Ok"               ; inizializzo paramentri
    push  ax
    mov   ax, 2101h                ; "!☺"
    push  ax

    CALL f


    mov ah, 4ch                 ; ritorno al sistema operativo
    int 21h

; eventuali procedure
f proc
    PUSH BP
    MOV BP, SP
    ADD SP, -2          ; 2 byte di variabili locali

    ;print Ok
    MOV AH, 02h
    MOV DL, [BP + 7]    ; Primo parametro
    INT 21h
    MOV DL, [BP + 6]    ; Secondo parametro
    INT 21h
    MOV DL, [BP + 5]    ; Terzo parametro
    INT 21h
    MOV DL, [BP + 4]    ; Quarto parametro
    INT 21h
    MOV DL, 10          ; New line
    INT 21h



    MOV SP, BP
    POP BP
    RET 4               ; 4 perche' ho 4 byte di parametri
f endp
       
    END   start