from utils.calculate_child_indices import calculate_child_indices
from utils.max_child import max_child_value_and_index
from utils.swap import swap
from utils.heapify_down import heapify_down

def fill_node_holes(heap_array, spawn_exponent, longest_ancestry, generation=0, parent_index=1):
  if generation == len(longest_ancestry):
    heap_array.pop(longest_ancestry[generation-1])
    return heap_array
  child_indices = calculate_child_indices(parent_index, spawn_exponent, len(heap_array))
  [max_child_index, _] = max_child_value_and_index(heap_array, child_indices)
  ideal_child_index_for_filling = longest_ancestry[generation]
  if max_child_index != ideal_child_index_for_filling:
    swap(heap_array, max_child_index, ideal_child_index_for_filling)
    heap_array = heapify_down(heap_array, max_child_index, spawn_exponent)
  swap(heap_array, parent_index, ideal_child_index_for_filling)
  return fill_node_holes(heap_array, spawn_exponent, longest_ancestry, generation+1, ideal_child_index_for_filling)