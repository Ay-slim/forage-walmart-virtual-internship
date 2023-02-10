def swap(array, first_index, second_index):
  temp = array[first_index]
  array[first_index] = array[second_index]
  array[second_index] = temp
  return array