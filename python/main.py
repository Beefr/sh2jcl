
from Job import Job

commandsFile='data.txt' # specifies what commands should be interpreted

outputFileName='copy' # specifies the name that we want to be generated
extension='job' # specifies the extension that we want  (.jcl .job .prc)
#fileName="$outputFileName.$extension"


def __main__(commandsFile, outputFileName, extension):
	print("Generating "+extension+" file from "+commandsFile+"\n\n")

	match extension:
		case 'jcl':
			return 'jcl'

		case 'job':
			return Job(commandsFile,outputFileName).generateFile()

		case 'prc':
			return 'prc' 

		case _:
			return ''			 




print(__main__(commandsFile, outputFileName, extension))