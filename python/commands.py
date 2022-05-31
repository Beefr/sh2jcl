

class Commands(object):

	def __init__(self, command, parameters):
		self._command=command
		self._parameters=parameters


	def generateText(self):
		return self.dictionnaire()




	def dictionnaire(self):

		match self._command:
			case 'copy': #input, output
				return self.copy(self._parameters[0], self._parameters[1])

			case 'donothing': 
				return self.donothing()

			case 'unique': #input, output
				return self.unique(self._parameters[0], self._parameters[1])

			case 'first': #input, output, rows
				return self.first(self._parameters[0], self._parameters[1], self._parameters[2])

			case 'sort': #input, output
				return self.sort(self._parameters[0], self._parameters[1])

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


	def first(self, input, output, records):
		text="\n//*"
		text=text+"\n//FIRST    EXEC PGM=ICETOOL"
		text=text+"\n//TOOLMSG  DD SYSOUT=*"
		text=text+"\n//DFSMSG   DD SYSOUT=*"
		text=text+"\n//IN1      DD DSN="+input+",DISP=SHR"
		text=text+"\n//OUT1	   DD DSN="+output+",DISP=SHR"
		text=text+"\n//TOOLIN   DD *"
		text=text+"\n  COPY FROM(IN1) TO(OUT1) USING(CTL1)"
		text=text+"\n/*"
		text=text+"\n//CTL1CNTL DD *"
		text=text+"\n  OPTION STOPAFT="+records
		text=text+"\n/*"
		return text




	def sort(self, input, output):
		text="\n//*"
		text=text+"\n//SORT     EXEC PGM=SORT"
		text=text+"\n//SYSOUT   DD SYSOUT=*"
		text=text+"\n//SORTIN   DD DSN="+input+",DISP=SHR"
		text=text+"\n//SORTOUT  DD DSN="+output+","
		text=text+"\n//      DISP=(NEW,CATLG,DELETE),UNIT=SYSDA,"
		text=text+"\n//      SPACE=(CYL,(1,4),RLSE),"
		text=text+"\n//      DCB=(RECFM=FB,LRECL=80,BLKSIZE=0)"
		text=text+"\n//SYSIN    DD *"
		text=text+"\n  SORT FIELDS=(1,6,CH,A)"
		text=text+"\n/*"
		return text






















































