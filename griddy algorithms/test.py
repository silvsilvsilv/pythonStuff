charFrequency = 1
y = ['a', 'a', 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
charFreqDict = {}

# for i in range(1,len(y),1):
# 	print(y[i])
print(y[-1])
for i in range(1,len(y),1):
		
		# sets char as key and charFrequency as value if not in dict
		charFreqDict.setdefault(y[i],charFrequency)

		if y[i] == y[i-1]:
			charFrequency += 1
			charFreqDict[y[i]] = charFrequency 
		elif y[i] != y[i-1]:
			charFrequency = 1
			charFreqDict[y[i]] = charFrequency 


for x in range(1,len(y),1):
	if x == 1:
		print(charFreqDict.get(y[x]),y[x])
		
	if y[x] != y[x-1]:
		print(charFreqDict.get(y[x]), y[x])
		
# print(charFreqDict)