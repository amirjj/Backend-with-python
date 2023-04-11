import threading
import queue
import requests


q = queue.Queue()


def get_page(number):

	# while q.empty(): # race condition

	while True:
		url = q.get()
		try:
			response = requests.get(url)
		except:
			print("Eroor")

		print(f"worker {number} \t get completed {url} \t queue size {q.qsize()} .")
		q.task_done()
		if q.empty():
			break


if __name__ == "__main__":

	links = [
		'https://google.com',
		'https://www.time.ir/'
	] * 10

	for link in links:
		q.put(link)

	threads = list()

	for i in range(4):
		tr = threading.Thread(target=get_page, args=(i, ))
		threads.append(tr)
		# tr.setDaemon(True)
		tr.start()

	q.join()

	# for tr in threads:
	# 	tr.join()

	print("Threads finished")
