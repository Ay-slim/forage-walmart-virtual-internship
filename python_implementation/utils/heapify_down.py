from utils.calculate_child_indices import calculate_child_indices
from utils.swap import swap
from utils.max_child import max_child_value_and_index

def heapify_down(heap_array, parent_index, spawn_exponent):
  child_indices = calculate_child_indices(parent_index, spawn_exponent, len(heap_array))
  if(len(child_indices) < 1):
    return heap_array
  [max_child_index, max_child_value] = max_child_value_and_index(heap_array, child_indices)
  if max_child_value > heap_array[parent_index]:
    heap_array = swap(heap_array, max_child_index, parent_index)
  return heapify_down(heap_array, max_child_index, spawn_exponent)