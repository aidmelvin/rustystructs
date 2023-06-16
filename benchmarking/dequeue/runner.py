
import random
import rustystructs
import time
from benchmarking.dequeue.dequeue_python import DequePython


class BenchmarkDeque:
    @staticmethod
    def performance_test():
        print('Starting Integer Deque Performance Test')
        runtimes = []
        sizes = [1000, 10000, 100000, 250000, 500000]
        for num_elements in sizes:
            current_size_runtime = []
            values = [random.randint(1, 10000) for _ in range(num_elements)]

            deque = rustystructs.Dequeue(int)

            start_time = time.time()

            for value in values:
                deque.append_start(value)

            for expected_value in reversed(values):
                assert deque.pop_head() == expected_value

            end_time = time.time()

            # print('Rust Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            deque = DequePython()

            start_time = time.time()

            for value in values:
                deque.add_front(value)

            for expected_value in reversed(values):
                assert deque.remove_front() == expected_value

            end_time = time.time()

            # print('Python Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            runtimes.append(current_size_runtime.copy())

        print('Num Elements\tRust\tPython')
        for one_size, size in zip(runtimes, sizes):
            print(f'{size}\t{one_size[0]}\t{one_size[1]}')

