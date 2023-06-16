
from stack.runner import BenchmarkStack
from heap.runner import BenchmarkHeap
from dequeue.runner import BenchmarkDeque

if __name__ == '__main__':
    BenchmarkStack.performance_test()
    BenchmarkHeap.performance_test()
    BenchmarkDeque.performance_test()
