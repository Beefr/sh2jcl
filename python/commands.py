

class Commands(object):

	def __init__(self, command, parameters):
		self._command=command
		self._parameters=parameters


	def generateText(self):
		return self.dictionnaire()




	def dictionnaire(self):

		match self._command:
			case 'copy':
				return self.copy(self._parameters[0], self._parameters[1])

			case _:
				return ''


	def copy(self, input, output):
		text=""
		text=text+"\n//COPY EXEC PGM=IEBGENER" 
		text=text+"\n//SYSIN DD DUMMY"
		text=text+"\n//SYSPRINT DD SYSOUT=*"
		text=text+"\n//SYSUT1 DD DSN="+input+",DISP=SHR"
		text=text+"\n//SYSUT2 DD DSN="+output+","
		text=text+"\n//        DISP=(MOD,CATLG,DELETE), UNIT=DISK1,"
		text=text+"\n//        SPACE=(TRK,20,10),RLSE),"
		return text