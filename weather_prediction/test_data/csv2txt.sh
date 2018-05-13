#!/bin/bash


parsing(){
D=(`ls | grep SURF`)
i=0
for data in ${D[@]} ; do
	grep -v hPa ${data}  | sed 's/-\|:\| //g'  |	awk -F ',' '{printf("%s,%s,%s,%s,%s,%s,%s\n",$2,$3,$4,$6,$5,$9,$8)}' > test_data0${i}.txt & 
	i=$((${i}+1))
done
wait 
}

prep(){
	rm test_data &> /dev/null ; touch test_data
	for i in {0..4} ; do
		python3 preprocessing.py test_data0${i}.txt >> test_data
	done
}



main(){
	parsing
	prep
}

prep

echo Done.
