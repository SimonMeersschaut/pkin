@echo off


set project=ckin
REM --------------

set Mydir=%~d0%~p0
set Myfile=%~n0%~x0

rem the orginal command of Kai was 
rem "gcc -Wfatal-errors  %Mydir%ckin.c %Mydir%get_element.c -lm -o %Mydir%%project%.exe 2> %Mydir%error.txt"
rem but not totally clear what the -lm stands for

gcc -Wfatal-errors  %Mydir%ckin.c %Mydir%get_element.c -o %Mydir%%project%.exe 2> %Mydir%error.txt
call :CheckEmpty "%Mydir%error.txt"
goto:eof



:Install
rem move     %Mydir%%project%.exe   C:\mcaiba\Optimion\bin\ > NUL
move     %Mydir%%project%.exe   C:\soft\ib_bin\ > NUL
del %Mydir%error.txt
echo   %Mydir%%project%.exe installed
goto:eof

:CheckEmpty
REM error.txt is empty
    if %~z1 EQU 0 goto Install
REM error.txt is not empty
    if %~z1 NEQ 0 Type %Mydir%error.txt
    if %~z1 NEQ 0 pause
echo.
goto:eof