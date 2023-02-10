import unittest
from utils.swap import swap
from utils.calculate_parent_index import calculate_parent_index

class TestUtils(unittest.TestCase):
  def test_swap_util(self):
    sampleArray = ['a', 'b', 'c', 'd', 'e']
    swappedArray = swap(sampleArray, 1, 3)
    self.assertTrue(swappedArray[1] == 'd' and swappedArray[3] == 'b')
  def test_parent_index_calculation(self):
    parent_index1 = calculate_parent_index(11, 2)
    parent_index2 = calculate_parent_index(14, 2)
    parent_index3 = calculate_parent_index(21, 2)
    parent_index4 = calculate_parent_index(25, 3)
    parent_index5 = calculate_parent_index(24, 3)
    parent_index6 = calculate_parent_index(21, 3)
    print(parent_index1, parent_index2, parent_index3, 'PARENT INDICESSS')
    self.assertTrue(parent_index1 == 3 and parent_index2 == 4 and parent_index3 == 5 and parent_index4 == 3 and parent_index5 == 3 and parent_index6 == 3)
if __name__ == '__main__':
    unittest.main(verbosity=2)