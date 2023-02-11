def max_child_value_and_index(heap_array, child_indices):
  child_values = list(map(lambda child_index: heap_array[child_index], child_indices))
  max_child_value = max(child_values)
  max_child_index = child_indices[child_values.index(max_child_value)]
  return [max_child_index, max_child_value]