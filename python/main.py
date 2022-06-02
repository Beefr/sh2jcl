
from interface import Interface

Interface()


'''
commandsFile='data.txt' # specifies what commands should be interpreted

outputFileName='copy' # specifies the name that we want to be generated
extension='job' # specifies the extension that we want  (.jcl .job .prc)
#fileName="$outputFileName.$extension"


def __main__(commandsFile, outputFileName, extension):
	print("Generating "+extension+" file from "+commandsFile+"\n\n")

	match extension:
		case 'jcl':
			return Jcl(commandsFile,outputFileName).generateFile()

		case 'job':
			return Job(commandsFile,outputFileName).generateFile()

		case 'prc':
			return Prc(commandsFile,outputFileName).generateFile() 

		case _:
			return ''			 

'''





"""
copie d'un dataset 0 vers le 1 
case 'copy': #input, output
return self.copy(self._parameters[0], self._parameters[1])

ne fait rien
case 'donothing': 
return self.donothing()

supprime les elements redondants de 0 et mets le resultat dans 1
case 'unique': #input, output
return self.unique(self._parameters[0], self._parameters[1])

récupère les rows premiers elements de 0 et les met dans 1
case 'first': #input, output, rows
return self.unique(self._parameters[0], self._parameters[1], self._parameters[2])

trie les elements de 0 et les met dans 1
case 'sort': #input, output
return self.unique(self._parameters[0], self._parameters[1])


"""



