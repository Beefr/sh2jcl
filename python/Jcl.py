
from JCLFile import JCLFile

class Jcl(JCLFile):


	def __init__(self, commandsFile, outputFileName):
		super().__init__(commandsFile, outputFileName)



	def beginning(self):
		return ""


	def end(self):
		return ""