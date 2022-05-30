
from JCLFile import JCLFile

class Job(JCLFile):


	def __init__(self, commandsFile, outputFileName):
		super().__init__(commandsFile, outputFileName)



	def beginning(self):
		return "//"+self._outputFileName+" JOB CLASS=A,MSGCLASS=A,MSGLEVEL=(1,1),NOTIFY=$SYSUID"