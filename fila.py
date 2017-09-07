import random

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

'''1 a 20 paginas impressas por impressao
		10 alunos em cada hora. cada aluno realize duas impressoes
		20 impressoes por hora = 1 impressao a cada 180 segundos (probabilidade de ocorrer uma impressao em um dado segundo)	'''

class Printer:
	def __init__(self, ppm):
		self.page_rate = ppm
		self.current_task = None
		self.time_remaining = 0

	def tick(self):
		if self.current_task != None:
			self.time_remaining = self.time_remaining - 1
			if self.time_remaining <= 0:
				self.current_task = None

	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	def start_next(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def get_stamp(self):
		return self.timestamp

	def get_pages(self):
		return self.pages

	def wait_time(self, current_time):
		return current_time - self.timestamp

def simulation(num_seconds, pages_per_minute, num_students, num_task_per_student):
	def new_print_task():
		num_seconds_to_start_each_task = 3600//(num_students*num_task_per_student)
		num = random.randrange(1,num_seconds_to_start_each_task+1)
		if num == num_seconds_to_start_each_task:
			return True
		else:
			return False

	lab_printer = Printer(pages_per_minute)
	print_queue = Queue()
	waiting_times = []

	for current_second in range(num_seconds):
		if new_print_task():
			task = Task(current_second)
			print_queue.enqueue(task)

		if (not lab_printer.busy() and (not print_queue.is_empty())):
			next_task = print_queue.dequeue()
			waiting_times.append(next_task.wait_time(current_second))
			lab_printer.start_next(next_task)

		lab_printer.tick()

	average_wait = sum(waiting_times) / len(waiting_times)
	print("Average wait %6.2f secs %3d tasks remaining." \
		% (average_wait, print_queue.size()))

for i in range(10):
	simulation(3600, 5, 10, 2)