def calculate_parent_index(child_index, spawn_exponent):
  max_num_of_children = 2**spawn_exponent
  remainder = child_index % max_num_of_children
  short_fall = max_num_of_children - remainder
  divisor = child_index - remainder if remainder in [0, 1] else child_index + short_fall
  return int(divisor / max_num_of_children)