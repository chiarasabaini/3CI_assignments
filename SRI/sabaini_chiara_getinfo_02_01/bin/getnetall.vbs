' List Network Adapters Properties

' Author: Sabaini Chiara 3CI - email: 18762@studenti.marconiverona.edu.it
' Version: 01.02
' Date: 2020-05-17

'Log

Wscript.Echo "Start time: " & Now()
Wscript.Echo

' Error handling

On Error Resume Next

' Variables

StartTime = Timer()

Dim strComputer
strComputer = "."

' Objects

Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colNetworkInfo = objWMIService.ExecQuery ("Select * from Win32_NetworkAdapterConfiguration")

' Loop that prints the selected properties

For Each objItem in colNetworkInfo
    Wscript.Echo "Caption: " & objItem.Caption
    Wscript.Echo "Description: " & objItem.Description
    Wscript.Echo "DHCP: " & objItem.DHCPEnabled
    Wscript.Echo "IP Address: " & objItem.IPAddress
    Wscript.Echo "MACAddress: " & objItem.MACAddress
    Wscript.Echo "Service Name: " & objItem.ServiceName
    Wscript.Echo "Setting ID: " & objItem.SettingID
    Wscript.Echo "Index in Interface: " & objItem.InterfaceIndex
    Wscript.Echo
Next

' Log

Wscript.Echo "End time: " & Now()

EndTime = Timer()
Wscript.Echo "Execution time: " & FormatNumber(EndTime - StartTime, 15) & "s"