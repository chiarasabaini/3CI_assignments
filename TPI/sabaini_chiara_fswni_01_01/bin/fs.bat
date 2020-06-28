@ECHO OFF
REM GET INFORMATION ABOUT OS, DISKS DRIVE
REM AND LOGICAL DISKS USING WMIC

REM REDIRECTING OUTPUTS IN .TXT FILES
CD ..\log
WMIC /output:os.txt os get caption, csname, serialnumber, version, windowsdirectory
WMIC /output:dd.txt diskdrive get caption, name, description, size, model, deviceid
WMIC /output:ld.txt logicaldisk get caption, filesystem, size, drivetype

REM REDIRECTING OUTPUTS IN .HTML FILES
CD ..\web
WMIC /output:os.html os get caption, csname, serialnumber, version, windowsdirectory /format:htable
WMIC /output:dd.html diskdrive get caption, name, description, size, model, deviceid /format:htable
WMIC /output:ld.html logicaldisk get caption, filesystem, size, drivetype /format:htable