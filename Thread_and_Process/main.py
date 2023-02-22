"""
The basic difference between multi-thread and multi-process is that:
-Multi-thread work on shared memory and Multi-process work on single memeory.
    as a result you can run more threads on each process.

Use Multi-Thread for IO bound
Use Multi-Thread for CPU bound
Using wrong mechanism will add more even overhead
Python Interpreter is Single-Thread and Single CPU by default
"""
