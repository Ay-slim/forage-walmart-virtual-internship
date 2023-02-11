from utils.calculate_child_indices import calculate_child_indices
from utils.swap import swap

def heapify_down(heap_array, parent_index, spawn_exponent):
  child_indices = calculate_child_indices(parent_index, spawn_exponent, len(heap_array))
  if(len(child_indices) < 1):
    return heap_array
  child_values = list(map(lambda child_index: heap_array[child_index], child_indices))

  max_child_value = max(child_values)
  max_child_index = child_indices[child_values.index(max_child_value)]
  if max_child_value > heap_array[parent_index]:
    heap_array = swap(heap_array, max_child_index, parent_index)
  return heapify_down(heap_array, max_child_index, spawn_exponent)