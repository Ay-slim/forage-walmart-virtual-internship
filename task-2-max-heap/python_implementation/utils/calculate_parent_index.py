def calculate_parent_index(child_index, spawn_exponent):
  max_num_of_children = 2**spawn_exponent
  remainder = child_index % max_num_of_children
  divisor = child_index - max_num_of_children if remainder == 0 else child_index - remainder
  return int(divisor / max_num_of_children)