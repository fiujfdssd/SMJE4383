top_num_str = input("What is the uppert number for the range: ")
top_num = int(top_num_str)
number=2
while number <= top_num:

	divisor = 1
	sum_of_divisor = 0
	while divisor < number:
		if number % divisor == 0:
			sum_of_divisor = sum_of_divisor + divisor
		divisor = divisor + 1
	
	if number == sum_of_divisor :
		print(number, " is perfect")
	if number < sum_of_divisor :
		print(number, " is abundant")
	if number > sum_of_divisor :
		print(number, " is deficient")
	number += 1
