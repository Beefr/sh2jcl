
input=$1
output=$2

echo "//COPY EXEC PGM=IEBGENER" 
echo "//SYSIN DD DUMMY"
echo "//SYSPRINT DD SYSOUT=*"
echo "//SYSUT1 DD DSN=$input,DISP=SHR"
echo "//SYSUT2 DD DSN=$output,"
echo "//        DISP=(MOD,CATLG,DELETE), UNIT=DISK1,"
echo "//        SPACE=(TRK,20,10),RLSE),"

