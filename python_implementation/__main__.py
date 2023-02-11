from utils.heapify_up import heapify_up
from utils.fill_node_holes import fill_node_holes
from utils.generate_longest_ancestry import generate_longest_ancestry
class PowerOfTwoMaxHeap:
  def __init__(self, spawn_exponent):
    self.spawn_exponent = spawn_exponent
    self.heap_array = [None]
  def insert(self, node_value):
    if(len(self.heap_array) == 1):
      self.heap_array.append(node_value)
      return self.heap_array[1:]
    else:
      self.heap_array.append(node_value)
      new_node_index = len(self.heap_array) - 1
      heapified_new_heap = heapify_up(self.heap_array, new_node_index, new_node_index, self.spawn_exponent)
      self.heap_array = heapified_new_heap
      return heapified_new_heap[1:]
  def pop_max(self):
    if(len(self.heap_array)==2):
      return self.heap_array.pop(1)
    else:
      max_element_index = self.heap_array[1]
      longest_ancestry = generate_longest_ancestry(self.spawn_exponent, self.heap_array)
      self.heap_array = fill_node_holes(self.heap_array, self.spawn_exponent, longest_ancestry)
      return max_element_index
    


# example = PowerOfTwoMaxHeap(1)
# print(example.insert(8)) #[8]
# print(example.insert(2)) #[8, 2]
# print(example.insert(9)) #[9, 2, 8]
# print(example.insert(4)) #[9, 4, 8, 2]
# print(example.insert(15)) #[15, 9, 8, 2, 4]
# print(example.insert(3)) #[15, 9, 8, 2, 4, 3]
# print(example.insert(1)) #[15, 9, 8, 2, 4, 3, 1]
# print(example.insert(7)) #[15, 9, 8, 7, 4, 3, 1, 2]
# print(example.pop_max())
# print(example.heap_array)

