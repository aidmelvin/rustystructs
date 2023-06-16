
import sys


class MaxHeapPython:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def remove_top(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        self._swap(0, len(self.heap) - 1)
        maxValue = self.heap.pop()
        self._sift_down(0)
        return maxValue

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._sift_up(parent_index)

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index

        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# class MaxHeapPython:
#     def __init__(self, maxsize):
#         self.maxsize = maxsize
#         self.size = 0
#         self.Heap = [0] * (self.maxsize + 1)
#         self.Heap[0] = sys.maxsize
#         self.FRONT = 1
#
#     # Function to return the position of
#     # parent for the node currently
#     # at pos
#     def parent(self, pos):
#         return pos // 2
#
#     # Function to return the position of
#     # the left child for the node currently
#     # at pos
#     def leftChild(self, pos):
#         return 2 * pos
#
#     # Function to return the position of
#     # the right child for the node currently
#     # at pos
#     def rightChild(self, pos):
#         return (2 * pos) + 1
#
#     # Function that returns true if the passed
#     # node is a leaf node
#     def isLeaf(self, pos):
#
#         if pos >= (self.size // 2) and pos <= self.size:
#             return True
#         return False
#
#     # Function to swap two nodes of the heap
#     def swap(self, fpos, spos):
#
#         self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
#                                             self.Heap[fpos])
#
#     # Function to heapify the node at pos
#     def maxHeapify(self, pos):
#         # If the node is a non-leaf node and smaller
#         # than any of its child
#         if not self.isLeaf(pos):
#             if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
#                     self.Heap[pos] < self.Heap[self.rightChild(pos)]):
#
#                 # Swap with the left child and heapify
#                 # the left child
#                 if (self.Heap[self.leftChild(pos)] >
#                         self.Heap[self.rightChild(pos)]):
#                     self.swap(pos, self.leftChild(pos))
#                     self.maxHeapify(self.leftChild(pos))
#
#                 # Swap with the right child and heapify
#                 # the right child
#                 else:
#                     self.swap(pos, self.rightChild(pos))
#                     self.maxHeapify(self.rightChild(pos))
#
#     # Function to insert a node into the heap
#     def add(self, element):
#         if self.size >= self.maxsize:
#             return
#         self.size += 1
#         self.Heap[self.size] = element
#
#         current = self.size
#
#         while (self.Heap[current] >
#                self.Heap[self.parent(current)]):
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
#
#     # Function to remove and return the maximum
#     # element from the heap
#     def remove_top(self):
#         popped = self.Heap[self.FRONT]
#         self.Heap[self.FRONT] = self.Heap[self.size]
#         self.size -= 1
#         self.maxHeapify(self.FRONT)
#
#         return popped

# class HeapPython:
#     def __init__(self, is_min):
#         self.is_min_heap = is_min
#         self.data = []
#
#     def add(self, value):
#         self.data.append(value)
#         index = len(self.data) - 1
#         self.sift_up(index)
#
#     def remove_top(self):
#         if not self.data:
#             return None
#
#         top = self.data.pop(0)
#         self.sift_down(0)
#         return top
#
#     def is_empty(self):
#         return len(self.data) == 0
#
#     def size(self):
#         return len(self.data)
#
#     def sift_up(self, index):
#         while index > 0:
#             parent_index = (index - 1) // 2
#
#             if self.is_min_heap and self.data[parent_index] <= self.data[index]:
#                 break
#
#             if not self.is_min_heap and self.data[parent_index] >= self.data[index]:
#                 break
#
#             self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
#             index = parent_index
#
#     def sift_down(self, index):
#         size = len(self.data)
#         while index < size:
#             left_child_index = 2 * index + 1
#             right_child_index = 2 * index + 2
#
#             smallest = index
#             if self.is_min_heap:
#                 if left_child_index < size and self.data[left_child_index] < self.data[smallest]:
#                     smallest = left_child_index
#                 if right_child_index < size and self.data[right_child_index] < self.data[smallest]:
#                     smallest = right_child_index
#             else:
#                 if left_child_index < size and self.data[left_child_index] > self.data[smallest]:
#                     smallest = left_child_index
#                 if right_child_index < size and self.data[right_child_index] > self.data[smallest]:
#                     smallest = right_child_index
#
#             if smallest == index:
#                 break
#
#             self.data[smallest], self.data[index] = self.data[index], self.data[smallest]
#             index = smallest
