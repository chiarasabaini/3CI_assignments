' List Network Protocols and Clients

' Author: Sabaini Chiara 3CI - email: 18762@studenti.marconiverona.edu.it
' Version: 01.01
' Date: 2020-05-16

On Error Resume Next

' Variables

Dim strComputer
strComputer = "."

' Objects

Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colNetProtocol = objWMIService.ExecQuery ("Select * from Win32_NetworkProtocol")
Set colNetClient = objWMIService.ExecQuery ("Select * from Win32_NetworkClient")


' Loops that print the selected properties

For Each objItem in colNetProtocol
    Wscript.Echo "Caption: " & objItem.Caption
    Wscript.Echo "Description: " & objItem.Description
    Wscript.Echo "Install date: " & objItem.InstallDate
    Wscript.Echo "Status: " & objItem.Status
    Wscript.Echo "Guarantees delivery: " & objItem.GuaranteesDelivery
    Wscript.Echo "Name: " & objItem.Name
    Wscript.Echo "Maximum address size: " & objItem.MaximumAddressSize
    Wscript.Echo "Maximum message size: " & objItem.MaximumMessageSize
    Wscript.Echo
Next

For Each objItem in colNetClient
    Wscript.Echo "Caption: " & objItem.Caption
    Wscript.Echo "Description: " & objItem.Description
    Wscript.Echo "Install date: " & objItem.InstallDate
    Wscript.Echo "Status: " & objItem.Status
    Wscript.Echo "Manufacturer: " & objItem.Manufacturer
    Wscript.Echo "Name: " & objItem.Name
    Wscript.Echo
Next
