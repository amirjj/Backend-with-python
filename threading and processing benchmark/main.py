import sys

from process import multi_process
from utils import DEFAULT_NUMBERS, is_prime
from thread import multi_thread


def run_normaly():
	for number in DEFAULT_NUMBERS:
		is_prime(number)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		run_normaly()
	elif sys.argv[1] == '-t':
		multi_thread()
	elif sys.argv[1] == '-p':
		multi_process()
