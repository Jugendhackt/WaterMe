#SerialPort = 0
Port$ = "COM9"
Global Msg$
Global Text$
Global *Buffer = AllocateMemory(1024)

OpenConsole("Serial: "+Port$)
Procedure RetrieveResponse() 
	Msg$ = ""
	Text$ = ""
	Repeat
		While AvailableSerialPortInput(#SerialPort) > 0
			If ReadSerialPortData(#SerialPort, @Buffer, 1) ; Read Byte
				Text$ = Text$ + Chr(Buffer)
			EndIf
			*Buffer = AllocateMemory(1024)
		Wend
		If Text$
			PrintN(Text$)
			Text$ = ""
		EndIf
		
		Delay(500)
	ForEver
EndProcedure

Repeat
If OpenSerialPort(#SerialPort, Port$, 115200, #PB_SerialPort_NoParity, 8, 1, #PB_SerialPort_NoHandshake, 1024, 1024)
	Repeat
		While AvailableSerialPortOutput(#SerialPort)
		Wend 
		RetrieveResponse()  
		PrintN(Msg$)
	ForEver
	CloseSerialPort(#SerialPort)
Else
	PrintN("Can´t open "+Port$)
EndIf
ForEver