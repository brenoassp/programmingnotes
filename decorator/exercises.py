# https://python.g-node.org/python-autumnschool-2010/_media/materials/advanced_python/exercises.pdf


# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
	def func_wrap(*args, **kwargs):
		all_args = []
		for arg in args:
			all_args.append(arg)
		for kwarg in kwargs:
			all_args.append(kwarg)
		print("You called {0}{1}".format(func.__name__, args))
		print("The result is: {0}".format(func(*args)))
		return func(args)
	return func_wrap

@logged
def func(*args):
	return 3 + len(args)

func(2,1 ,6)