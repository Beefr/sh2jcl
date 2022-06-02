
from tkinter import *
from Job import Job
from Jcl import Jcl
from Prc import Prc

class InterfaceMeta(type):


	_instances = {}


	def __call__(cls, *args, **kwargs):
		"""
		Possible changes to the value of the `__init__` argument do not affect
		the returned instance.
		"""
		if cls not in cls._instances:
		    instance = super().__call__(*args, **kwargs)
		    cls._instances[cls] = instance
		return cls._instances[cls]



class Interface(metaclass=InterfaceMeta):



	def __init__(self):
		self._root = Tk(className=" JCL Generator")
		self._root.geometry("1000x900")


		self._extensionListBox = Listbox(self._root, height=3)
		self._outputFileName = Text(self._root, height=1, width=20)
		self._arguments = Text(self._root, height=6, width=50)
		self._output = Text(self._root, height=40, width=100)
		self._generate = Button(self._root, text = "Generate", command = self.generate)
		self._save = Button(self._root, text = "Save", command = self.save)
		self.show()


		self._root.mainloop()


	def show(self):


		
		self._extensionListBox.insert(1, 'job')
		self._extensionListBox.insert(2, 'prc')
		self._extensionListBox.insert(3, 'jcl')
		self._extensionListBox.pack()

		
		self._outputFileName.insert(INSERT,"FILENAME")
		self._outputFileName.pack()

		self._arguments.insert(INSERT,"unique:user.dataset.input,temp1,\nsort:temp1,temp2,\nfirst:temp2,user.dataset.output,10,")
		self._arguments.pack()

		self._output.pack()

		self._generate.pack()

		self._save.pack()


	def generate(self):
		self._output.delete('1.0', END)
		
		extension=self.getExtension()
		if extension==None:
			return None

		outputFileName=self._outputFileName.get("1.0",END)
		if len(outputFileName)==1:
			self._output.insert(INSERT,"No output filename was entered")
			return None

		instance =Jcl(self._arguments.get("1.0",END),outputFileName)
		txt=instance.generateFile()
		self._output.insert(INSERT, txt)
		return 0


	def getExtension(self):
		choice=self._extensionListBox.curselection()
		extension=''

		if (len(choice)==0):
			self._output.insert(INSERT,"No extension was selected")
			return None
		else:
			match choice[0]:
				case 0:
					extension='job'
				case 1:
					extension='prc'
				case 2:
					extension='jcl'
				case _:
					extension=''
		return extension


	def save(self):
		f = open(self._outputFileName.get("1.0","end-1c")+"."+self.getExtension(), "w")
		f.write(self._output.get("1.0",END))
		f.close()





