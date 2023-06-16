import rustystructs
import unittest
import random

class TestDatastructures(unittest.TestCase):
    def test_heap_basic(self):
        my_heap = rustystructs.Heap(int, True)
        self.assertEqual(my_heap.is_empty(), True)
        self.assertEqual(my_heap.remove_top(), None)

    def test_min_heap_produces_sorted_values(self):
        # Generate an array of 1000 random values
        values = [random.randint(1, 10000) for _ in range(1000)]

        # Create an instance of the custom heap implementation
        heap = rustystructs.Heap(int, True)

        # Add values to the heap
        for value in values:
            heap.add(value)

        # Pop values from the heap and check their correctness
        for expected_value in sorted(values):
            assert heap.remove_top() == expected_value

    def test_max_heap_produces_sorted_values(self):
        # Generate an array of 1000 random values
        values = [random.randint(1, 10000) for _ in range(1000)]

        # Create an instance of the custom heap implementation
        heap = rustystructs.Heap(int, False)

        # Add values to the heap
        for value in values:
            heap.add(value)

        # Pop values from the heap and check their correctness
        for expected_value in sorted(values, reverse=True):
            assert heap.remove_top() == expected_value
    
    def test_dequeue_basic(self):
        my_dequeue = rustystructs.Dequeue(int)
        values = [random.randint(1, 10000) for _ in range(1000)]
        for value in values:
            my_dequeue.append_start(value)

        for expected_value in reversed(values):
            assert my_dequeue.pop_head() == expected_value
    
    def test_stack_basic(self):
        my_stack = rustystructs.Stack(int)
        values = [random.randint(1, 10000) for _ in range(1000)]
        for value in values:
            my_stack.add(value)
        
        for expected_value in reversed(values):
            assert expected_value == my_stack.pop()
        
        assert my_stack.peek() == None
        assert my_stack.pop() == None
    
    def test_throws_error_incorrect_argument(self):
        with self.assertRaises(TypeError):
            my_incorrect_heap = rustystructs.Heap(object, True)
        
        with self.assertRaises(TypeError):
            my_incorrect_stack = rustystructs.Stack(object)
        
        with self.assertRaises(TypeError):
            my_incorrect_queue = rustystructs.Dequeue(object)
        

if __name__ == '__main__':
    unittest.main()
