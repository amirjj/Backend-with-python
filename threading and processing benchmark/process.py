from multiprocessing import Pool
from utils import is_prime, DEFAULT_NUMBERS


def multi_process():
	pool = Pool(4)
	with pool:
		pool.map(is_prime, DEFAULT_NUMBERS)

	print("All processes finished")
