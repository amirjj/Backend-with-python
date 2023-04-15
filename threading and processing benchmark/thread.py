import threading
from queue import Queue
from utils import is_prime, DEFAULT_NUMBERS


q = Queue()


def show_is_prime(worker_id):
	while True:
		number = q.get()
		is_prime(number)
		q.task_done()
		if q.empty():
			break


def multi_thread():
	for num in DEFAULT_NUMBERS:
		q.put(num)

	threads = list()
	for i in range(6):
		t = threading.Thread(target=show_is_prime, args=(i, ))
		threads.append(t)
		t.setDaemon(True)
		t.start()

	print("Thread not joined yet")
	q.join()
	print("Threads finished")
