def output(name,**kwargs):
	print 'name: ',name
	for i in kwargs.keys():
		print i, ":",kwargs[i]

output("Denis",age=25,gender='M',location='Nairobi')

#checkout setattrs()
#checkout ** operator that unpacks a dictionary
#checkout **args