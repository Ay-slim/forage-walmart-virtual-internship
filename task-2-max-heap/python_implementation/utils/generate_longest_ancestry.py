from utils.calculate_parent_index import calculate_parent_index
from utils.calculate_child_indices import calculate_child_indices
from utils.max_child import max_child_value_and_index
def generate_longest_ancestry(spawn_exponent, heap_array, last_child_index=0, generation=1, longest_ancestry=[]):
  """
  Returns a list of indices from the last child to the second generation
  """
  if last_child_index in range(1, 2**spawn_exponent):
    return longest_ancestry
  if generation == 1:
    last_child_index = len(heap_array) - 1
  parent_index = (calculate_parent_index(last_child_index, spawn_exponent))
  if generation == 1:
    #Ensure that the last index in the ancestry holds the highest value amongst its siblings.
    last_generation_child_indices = calculate_child_indices(parent_index, spawn_exponent, len(heap_array))
    [max_last_generation_child_index, _] = max_child_value_and_index(heap_array, last_generation_child_indices)
    longest_ancestry.append(max_last_generation_child_index)
  longest_ancestry.insert(0, parent_index)
  return generate_longest_ancestry(spawn_exponent, heap_array, parent_index, generation+1, longest_ancestry)

