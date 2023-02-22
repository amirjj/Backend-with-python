"""
In a process with couple of threads, just one thread will be run in a single time.
As Threads are shared memory, Python Interpreter prefer to execute one thread at a time.

Python is not thread-safe, and was originally designed with something called the GIL,
or Global Interpreter Lock, that ensures processes are executed serially on a computer’s CPU.
On the surface, this means Python programs cannot support multiprocessing.

GIL stop threads when they are using CPU not when they wait
All threads start and stop at almost same time
"""
import time
from time import sleep
import threading
import requests


def worker(number):
    t1 = time.time()
    sleep(2)
    t2 = time.time()
    print(f'worker {number} started at {t1}, finished at {t2}')


def get_page(url):
    print(f'Thread started {url}')
    try:
        response = requests.get(url)
    except:
        print(f'Error occured {url}')

    print(f'get completed {url}')


if __name__ == "__main__":
    # for i in range(5):
    #     worker(i)

    # for i in range(5000):
    #     """
    #     As this process is not CPU bound and it's just a wait all will start together
    #     """
    #     t = threading.Thread(target=worker, args=(i, ))
    #     t.start()

    urls = [
        'https://google.com',
        'https://yahoo.com'
    ] * 4

    # for url in urls:
    #     t = threading.Thread(target=get_page, args=(url, ))
    #     t.start()
    #
    # print('All threads started')

    threads = list()
    for link in urls:
        t = threading.Thread(target=get_page, args=(link, ))
        threads.append(t)
        t.setDaemon(True)
        """
        if main process finished stop the thread to prevent zambie threads. a hook bind threads to main process.
        """
        t.start()

    print("Before joininig")
    for tr in threads:
        # wait here to execution of all threads
        tr.join()

    print("After joininig")
