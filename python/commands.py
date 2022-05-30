

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

			case 'donothing':
				return self.donothing()

			case 'unique':
				return self.unique(self._parameters[0], self._parameters[1])

			case _:
				return ''


	def copy(self, input, output):
		text="\n//*"
		text=text+"\n//COPY     EXEC PGM=IEBGENER" 
		text=text+"\n//SYSIN    DD DUMMY"
		text=text+"\n//SYSPRINT DD SYSOUT=*"
		text=text+"\n//SYSUT1   DD DSN="+input+",DISP=SHR"
		text=text+"\n//SYSUT2   DD DSN="+output+","
		text=text+"\n//         DISP=(MOD,CATLG,DELETE), UNIT=DISK1,"
		text=text+"\n//         SPACE=(TRK,20,10),RLSE),"
		text=text+"\n//*"
		return text

	def donothing(self):
		text="\n//*"
		text=text+"\n//NOTHING  EXEC PGM=IEFBR14"
		text=text+"\n//*"
		return text


	def unique(self, input, output):
		text="\n//*"
		text=text+"\n//UNIQUE   EXEC PGM=SORT"
		text=text+"\n//SYSOUT   DD SYSOUT=*"
		text=text+"\n//SORTIN   DD DSN="+input+",DISP=SHR"
		text=text+"\n//SORTOUT  DD DSN="+output+",DISP=SHR"
		text=text+"\n//SYSIN    DD *"
		text=text+"\n  SORT FIELDS=(1,15,ZD,A)" #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		text=text+"\n  SUM FIELDS=NONE" #removes duplicates on fields specified in SORT FIELDS. 
		text=text+"\n/*" #In the above example, employee number is in the field position 1,15
		text=text+"\n//*" #The output file will contain the unique employee numbers sorted in ascending order.
		return text


	#def first(self, input, output):




































