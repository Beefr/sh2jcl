
from tkinter import *

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
		self._root.geometry("1000x500")


		self.show()


		self._root.mainloop()


	def show(self):


		extensionListBox = Listbox(self._root)
		extensionListBox.insert(1, 'job')
		extensionListBox.insert(2, 'prc')
		extensionListBox.insert(3, 'jcl')
		extensionListBox.pack()


Interface()






