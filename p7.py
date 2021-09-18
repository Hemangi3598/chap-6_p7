# wapf to find fact of an integer

def fact(num):
	f = 1
	for i in range(1, num+1):
		f = f * i
	return f
num = int(input(" enter a number "))
if num < 0:
	print("invalid input")
else:
	ans = fact(num)
	print("fact = ", ans)