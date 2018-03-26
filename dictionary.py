import operator

def dic(count, line)
	data={}
	for e in line:
		key=e.get("name")
		value=e.get("price")
		data[key]=value
		
	sorted_data=sorted(data.items(), key=operator.itemgetter(1),reverse=True)
	
	rtn_list=[]
	for i in range(0, count):
		rtn_list.append(sorted_data[i][0])
		
	print(rtn_list)