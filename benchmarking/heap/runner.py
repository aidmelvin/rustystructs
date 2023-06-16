
import time
import random
import rustystructs
from benchmarking.heap.heap_python import MaxHeapPython
import heapq


class BenchmarkHeap:
    @staticmethod
    def performance_test():
        print('Starting Integer Heap Performance Test')
        runtimes = []
        sizes = [1000, 10000, 100000, 250000, 500000, 1000000]
        for num_elements in sizes:
            current_size_runtime = []
            values = [random.randint(1, 10000) for _ in range(num_elements)]

            heap = rustystructs.Heap(int, False)

            start_time = time.time()

            for value in values:
                heap.add(value)

            for expected_value in sorted(values, reverse=True):
                assert heap.remove_top() == expected_value

            end_time = time.time()

            # print('Rust Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            heap = MaxHeapPython()

            start_time = time.time()

            for value in values:
                heap.add(value)

            for expected_value in sorted(values, reverse=True):
                assert heap.remove_top() == expected_value

            end_time = time.time()

            # print('Python Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))

            start_time = time.time()

            heap_values = values.copy()

            heapq.heapify(heap_values)

            for heapq_value, expected_value in zip(heapq.nlargest(num_elements, heap_values), sorted(values, reverse=True)):
                assert heapq_value == expected_value

            end_time = time.time()

            # print('Heapq Heap Execution Time: ', (end_time - start_time))
            current_size_runtime.append((end_time - start_time))
            runtimes.append(current_size_runtime.copy())

        print('Num Elements\tRust\tPython\tHeapq')
        for one_size, size in zip(runtimes, sizes):
            print(f'{size}\t{one_size[0]}\t{one_size[1]}\t{one_size[2]}')
