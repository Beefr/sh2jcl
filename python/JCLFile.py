
from commands import Commands
from abc import abstractmethod

class JCLFile(object):


	def __init__(self, commandsFile, outputFileName):
		self._commandsFile=commandsFile
		self._outputFileName=outputFileName
		self._text=self.generateFile()


	@abstractmethod
	def beginning(self):
		raise NotImplementedError("Hey, Don't forget to implement")


	def core(self):
		self._text=""
		with open(self._commandsFile) as f:
			lines = f.readlines()
			for line in lines:
				split=line.split(":")
				command=split[0]
				parameters=split[1].split(",")

				self._text=self._text+Commands(command, parameters).generateText()
		return self._text

	def coreV2(self):
		self._text=""
		for line in self._commandsFile.splitlines(): #contains the text in the TextBox
			split=line.split(":")
			command=split[0]
			parameters=split[1].split(",")

			self._text=self._text+Commands(command, parameters).generateText()
		return self._text

	def end(self):
		raise NotImplementedError("Hey, Don't forget to implement")

	def generateFile(self):		
		self._text=self.beginning()
		#self._text=self._text+self.core() #was implemented for interactions with the command line
		self._text=self._text+self.coreV2() # but now we have got an interface
		self._text=self._text+self.end()
		return self._text

	@property
	def commandsFile(self):
		return self._commandsFile

		
	@property
	def outputFileName(self):
		return self._outputFileName

		
	@property
	def text(self):
		return self._text

	@outputFileName.setter
	def outputFileName(self, outputFileName):
		self._outputFileName=outputFileName

	@commandsFile.setter
	def commandsFile(self, commandsFile):
		self._commandsFile=commandsFile

	
























