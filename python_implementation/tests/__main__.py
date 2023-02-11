import unittest
from utils.swap import swap
from utils.calculate_parent_index import calculate_parent_index
from utils.heapify_up import heapify_up
from utils.calculate_child_indices import calculate_child_indices
from utils.heapify_down import heapify_down
from utils.generate_longest_ancestry import generate_longest_ancestry
from utils.fill_node_holes import fill_node_holes
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
    self.assertTrue(parent_index1 == 3 and parent_index2 == 4 and parent_index3 == 5 and parent_index4 == 3 and parent_index5 == 3 and parent_index6 == 3)
  def test_heapify_up(self):
    test_heapified_array = heapify_up([None, 1, 9, 2, 3], 4, 4, 1)
    self.assertTrue(test_heapified_array == [None, 3, 9, 2, 1])
  def test_child_indices_generation(self):
    child_indices_power2 = calculate_child_indices(3, 2, 13)
    child_indices_power3 = calculate_child_indices(2, 3, 18)
    self.assertTrue(child_indices_power2 == [10, 11, 12] and child_indices_power3 == [10, 11, 12, 13, 14, 15, 16, 17])
  def test_heapify_down(self):
    heapify_down_test_array = [None, 1000, 500, 800, 700, 900, 850, 650, 620, 630, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 610, 615, 612]
    down_heapified_array = heapify_down(heapify_down_test_array, 2, 2)
    self.assertTrue(down_heapified_array == [None, 1000, 850, 800, 700, 900, 615, 650, 620, 630, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 610, 500, 612])
  # def test_longest_ancestry_squared(self):
  #   sample_heap_array = [None, 2000, 800, 700, 1000, 600, 500, 550, 480, 390, 220, 280, 290, 300, 150, 180, 170, 160]
  #   squared_ancestry = generate_longest_ancestry(2, sample_heap_array)
  #   print(squared_ancestry, 'SQUARED_ANCESTRY')
  #   #unary_ancestry = generate_longest_ancestry(1,sample_heap_array)
  #   # and unary_ancestry==[2,4,9,18]
  #   self.assertTrue(squared_ancestry==[4,15])
  # def test_longest_ancestry_unary(self):
    # sample_heap_array = [None, 2000, 800, 700, 1000, 600, 500, 550, 480, 390, 220, 280, 290, 300, 150, 180, 170, 160]
    # #squared_ancestry = generate_longest_ancestry(2, sample_heap_array)
    # unary_ancestry = generate_longest_ancestry(1,sample_heap_array)
    # print(unary_ancestry, 'UNARY ANCESTRY')
    # # and unary_ancestry==[2,4,9,18]
    # self.assertTrue(unary_ancestry==[2,4,8,16])
  # def test_fill_node_holes_straight(self):
  #   sample_heap_array_straight = [None, 2000, 800, 700, 1000, 600, 500, 550, 480, 390, 220, 280, 290, 300, 150, 180, 170, 160]
  #   longest_ancestry_straight = generate_longest_ancestry(2, sample_heap_array_straight)
  #   filled_heap_array_straight = [None, 1000, 800, 700, 180, 600, 500, 550, 480, 390, 220, 280, 290, 300, 150, 170, 160]
  #   func_resp_straight = fill_node_holes(sample_heap_array_straight, 2, longest_ancestry_straight)
  #   self.assertTrue(func_resp_straight==filled_heap_array_straight)
  def test_fill_node_holes_glitch(self):
    sample_heap_array_glitch = [None, 2000, 1000, 700, 800, 600, 900, 550, 480, 390, 220, 280, 290, 300, 150, 180, 170, 160]
    longest_ancestry_glitch = generate_longest_ancestry(2, sample_heap_array_glitch)
    filled_heap_array_glitch = [None, 1000, 900, 700, 180, 600, 800, 550, 480, 390, 220, 280, 290, 300, 150, 170, 160]
    func_resp_glitch = fill_node_holes(sample_heap_array_glitch, 2, longest_ancestry_glitch)
    self.assertTrue(func_resp_glitch==filled_heap_array_glitch)
if __name__ == '__main__':
    unittest.main(verbosity=2)