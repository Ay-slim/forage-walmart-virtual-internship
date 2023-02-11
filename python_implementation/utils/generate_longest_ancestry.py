from utils.calculate_parent_index import calculate_parent_index
def generate_longest_ancestry(spawn_exponent, heap_array_length=0, generation=1, longest_ancestry=[], child_index=None):
  """
  Returns a list of indices from the last child to the second generation
  """
  if child_index in range(2, ((2**spawn_exponent)+2)):
    return longest_ancestry
  if generation == 1:
    child_index = heap_array_length - 1
  parent_index = (calculate_parent_index(child_index, spawn_exponent))
  longest_ancestry.insert(0, parent_index)
  return generate_longest_ancestry(spawn_exponent, heap_array_length, generation+1, longest_ancestry, parent_index)
