def add(x,y):
	return x + y

y = lambda x,y:x+y
print(y(10,2))

def make_inc_lambda(n):
	return lambda x:x+n
y = make_inc_lambda(10)
print(y(20))

def is_even(n):
	return n%2 == 0
l = [2,12,5,7,8,8]
new_list = filter(is_even,l)
print(new_list)
another_list = filter(lambda x:x%2 == 0,l)
print(another_list)