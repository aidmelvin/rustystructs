
import random
import rustystructs
import time
from benchmarking.stack.stack_python import StackPython


class BenchmarkStack:
    @staticmethod
    def performance_test():
        print('Starting Integer Stack Performance Test')
        runtimes = []
        sizes = [1000, 10000, 100000, 250000, 500000, 1000000]
        for num_elements in sizes:
            current_size_runtime = []
            values = [random.randint(1, 10000) for _ in range(num_elements)]

            stack = rustystructs.Stack(int)

            start_time = time.time()

            for value in values:
                stack.add(value)

            for expected_value in reversed(values):
                assert stack.pop() == expected_value

            end_time = time.time()

            # print('Rust Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            stack = StackPython()

            start_time = time.time()

            for value in values:
                stack.push(value)

            for expected_value in reversed(values):
                assert stack.pop() == expected_value

            end_time = time.time()

            # print('Python Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            runtimes.append(current_size_runtime.copy())

        print('Num Elements\tRust\tPython')
        for one_size, size in zip(runtimes, sizes):
            print(f'{size}\t{one_size[0]}\t{one_size[1]}')

