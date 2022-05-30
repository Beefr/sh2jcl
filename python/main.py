
from Job import Job
from Jcl import Jcl
from Prc import Prc

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




print(__main__(commandsFile, outputFileName, extension))
print("____________________________________")

print(__main__('data2.txt', 'donothing', 'jcl'))
print("____________________________________")


print(__main__('data3.txt', 'unique', 'prc'))