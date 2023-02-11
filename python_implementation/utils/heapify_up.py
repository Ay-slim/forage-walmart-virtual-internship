from utils.calculate_parent_index import calculate_parent_index
from utils.swap import swap
def heapify_up(heap_array, current_child_index, child_value_index, spawn_exponent):
  """
  Recursively goes up the heap to ensure that the max heap requirement is satisfied
  - Specifiying child_value_index separately from current_child_index because we may not have to swap on every check
  - Also, need to pass the specific index as an argument rather than the value because there may be another index holding the same value somewhwere up the heap
  """
  if current_child_index == 1:
    return heap_array
  parent_index = calculate_parent_index(current_child_index, spawn_exponent)
  child_value = heap_array[child_value_index]
  if child_value > heap_array[parent_index]:
    heap_array = swap(heap_array, child_value_index, parent_index)
    child_value_index = parent_index
  return heapify_up(heap_array, parent_index, child_value_index, spawn_exponent)