f = open("input.txt", 'r')	
g = open("output.txt", 'w')
lines = f.read().splitlines()
for line in lines: 
	if len(line) > 10:
		line[0 - 10] 
	g.write(line)	

	