num_str = input ("Enter a +ve integer: ")
num = int(num_str)
count=0

print ("Starting with number: ",num)
print("Sequence is: ", end=' ')

while num > 1:
	
	if num % 2 :
		num = num*3 + 1
	else :
		num = num/2
	print (num,",", end=' ')
	
	count +=1
else:
	print()
	print("Sequence is ",count," numbers long")
