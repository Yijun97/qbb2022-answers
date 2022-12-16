for FA in *.fa; do 
	name=$(echo $FA |sed 's/.fa//');
		echo $FA; 
	NODE_ARRAY=( $(grep ">" $FA) )
	
	echo ""> ${name}.kraken.annotated
	for node in "${NODE_ARRAY[@]}";do
		#echo "first"
		#echo $node
		n=$(echo $node | sed 's/^.//' )
		grep $n assembly.kraken >> ${name}.kraken.annotated
	done
done
		
		
		
		
		
		
		