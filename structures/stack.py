# Stack data structure that allows list reversal for free.

def push(list, item):
	return list, item

def peek(list):
	_, value = list
	return value

def pop(list):
	previous, _ = list
	return previous
