from utils.calculate_parent_index import calculate_parent_index
from utils.swap import swap
from utils.last_occurence_index import final_index
def heapify_up(heap_array, current_child_index, new_child_value, spawn_exponent):
  """
  Recursively goes up the heap to ensure that the max heap requirement is satisfied
  - Specifiying child_value_index separately from current_child_index because we may not have to swap on every check
  - Also, need to pass the specific index as an argument rather than the value because there may be another index holding the same value somewhwere up the heap
  """
  if current_child_index == 0:
    return heap_array
  parent_index = calculate_parent_index(current_child_index, spawn_exponent)
  if new_child_value > heap_array[parent_index]:
    new_child_value_index = final_index(heap_array, new_child_value)
    heap_array = swap(heap_array, new_child_value_index, parent_index)
  return heapify_up(heap_array, parent_index, new_child_value, spawn_exponent)