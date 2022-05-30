#!bin/bash

commandsFile=$1 # specifies what commands should be interpreted

outputFileName=$2 # specifies the name that we want to be generated
extension=$3 # specifies the extension that we want  (.jcl .job .prc)
fileName="$outputFileName.$extension"
echo creating $fileName
echo
#touch $fileName


# creating the first part of the output file
case $extension in
	jcl)
		echo jcl
	;;
	
	job)
		echo "//$outputFileName JOB CLASS=A,MSGCLASS=A,MSGLEVEL=(1,1),kNOTIFY=\$SYSUID"
	;;
	
	prc)
		echo prc
	;;
esac

#reading the command file
while read line; do
	commandLine=$line
	command=$( echo $line|cut -d, -f1) #get the first field, the command field
	parameters=$( echo $line|cut -d, -f2)
	eval ./dictionnaire/$command.sh $parameters
done < $commandsFile







