
from JCLFile import JCLFile

class Prc(JCLFile):


	def __init__(self, commandsFile, outputFileName):
		super().__init__(commandsFile, outputFileName)



	def beginning(self):
		text="//CREFILE PROC"
		return text


	def end(self):
		return "\n//        PEND"