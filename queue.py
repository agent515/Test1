class Queue():
	
	
	def __init__(self, start=0, end=10):
		self.queue=[]
		self.start=start
		self.end=end-1
		
	def __str__(self):
		return self.queue
		
	def __iter__(self):
		return self.queue.__iter__()
	
	def push(self, val):
		if len(self.queue) >= self.end-1:
			print("Error")
		else: 
			self.queue.append(val)
			
	def pop(self):
		if len(self.queue) != self.start:
			return self.queue[0]
			self.start+=1
		else:
			return "Empty"
		
if __name__ == "__main__":
	queue=Queue()
	for i in range(0, 10):
		a=int(input("Enter a number: "))
		queue.push(a)
		
print("Initial queue: " + str(list(queue)))
print("pop(): " + str(queue.pop()))
print("Queue after pop: " + str(list(queue)))
