TITLE  

DOSSEG
.MODEL small

; definizione segmento di stack
.STACK 100h

; definizione segmento dati
.DATA
msg    db "Hi, I'm a Interrupt v02 ", 01h, 02h, "$" ; 01h and 02h are more than necessary
; definizione segmento codice

.CODE
start:
    MOV   AX, @DATA             ; inizializzazione registro
    MOV   DS, AX                ; di segmento DS

    ; Save last vector's table state
    MOV   AH, 35h
    MOV   AL, 81h
    INT   21h
    PUSH  ES
    PUSH  BX

    
    ; Make my interupt
    PUSH  CS
    LEA   AX, p
    PUSH  AX
    MOV   AH, 25h
    MOV   AL, 81h               ; The location of my interrupt, after I can use INT 81h to use it
                                ; (if you prefer another position, change the number with another one bigger or equal than 7Fh)
    PUSH AX

    CALL make_int

    INT 81h

    ;Restore
    PUSH  ES                    ; last CS
                                ;LEA   AX, p
    PUSH  BX                    ;AX
    MOV   AH, 25h
    MOV   AL, 81h               ; The location of my interrupt, after I can use INT 81h to use it
                                ; (if you prefer another position, change the number with another one bigger or equal than 7Fh)
    PUSH AX
    CALL make_int
    SUB SP, -4                  ; Remove ES & BX without save it

    ;End
    MOV AH, 4ch                 ; ritorno al sistema operativo

    INT 21h

; eventuali procedure
make_int proc
    PUSH BP
    MOV BP, SP
    ADD SP, -8   ; 4 local variable

    ; Save DS, DX, CS and AX
    MOV [BP-8], DS
    MOV [BP-6], AX
    MOV AX, DX
    MOV [BP-4], AX
    MOV AX, CS
    MOV [BP-2], AX

    ; Take all my parameters
    MOV AX, [BP+8]
    MOV DS, AX
    MOV DX, [BP+6]                  ; MOV AX, [BP+6] & MOV DX, AX
    MOV AX, [BP+4]

    ; Make my interupt
    INT 21h
    
    ; Reset my registers
    MOV AX, [BP-4]
    MOV DX, AX
    MOV AX, [BP-2]
    MOV AX, CS
    MOV AX, [BP-6]
    MOV DS, [BP-8]

    MOV SP, BP
    POP BP
    RET 8               ; 8 perche' ho 8 byte di parametri
make_int endp

p proc
    PUSH BP
    MOV BP, SP

    MOV AH, 09h
    LEA DX, msg

    INT 21h

    MOV SP, BP
    POP BP
    IRET
p endp
       
    END   start
    