def calculate_child_indices(parent_index, spawn_exponent, heap_array_length):
  max_num_of_children = 2**spawn_exponent
  first_child_index = (parent_index*max_num_of_children) + 1
  last_child_index = (parent_index*max_num_of_children) + max_num_of_children
  return [child_index for child_index in range(first_child_index, last_child_index+1) if child_index < heap_array_length]
