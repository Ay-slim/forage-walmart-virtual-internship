def final_index(heap_array, element):
  return max(index for index, item in enumerate(heap_array) if item == element)