#!bin/bash

commandsFile=$1 # specifies what commands should be interpreted

#reading the command file
while read line; do
	echo line
done < $commandsFile