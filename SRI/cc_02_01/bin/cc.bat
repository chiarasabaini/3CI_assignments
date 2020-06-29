@ECHO ON
REM executes the commands tasm, tlink and debug automatically

REM COPYING THE FILE THAT HAS TO BE COMPILED AND LINKED FROM SRC TO BIN

COPY ..\src\%1.asm ..\bin /y
CD ..\bin

REM TASM
TASM %1.asm

REM TLINK
TLINK %1

REM DELETING THE SUPERFLUOUS FILES
REM (if you need one of the feel free of commenting the following lines)
DEL %1.asm
DEL %1.obj
DEL %1.map

REM DEBUG 
REM (comment the next line if you just want to execute the program
REM  without debugging it)
DEBUG %1.exe

REM EXECUTE
%1