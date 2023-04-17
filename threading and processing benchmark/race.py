import threading


x = 0


def increment_x():
	global x
	for i in range(2000000):
		x += 1


def worker(lock):
	lock.acquire()
	increment_x()
	lock.release()


def start_thread():
	global x
	x = 0
	lock = threading.Lock()
	threads = list()
	for _ in range(3):
		tr = threading.Thread(target=worker, args=(lock, ))
		tr.start()
		threads.append(tr)

	for tr in threads:
		tr.join()


if __name__ == "__main__":
	for i in range(5):
		start_thread()
		print(f"Turn {i} finished, x = {x}")

	print("script finished")
