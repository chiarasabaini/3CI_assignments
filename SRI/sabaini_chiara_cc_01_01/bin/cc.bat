@ECHO ON
REM executes the commands tasm, tlink and debug automatically

REM TASM
TASM %1.asm

REM TLINK
TLINK %1

REM DEBUG (comment the next line if you just want to execute the program)
DEBUG %1.EXE

REM EXECUTE
%1