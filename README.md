### Custom heap implementation

- Uses an array and its indices to implement a max heap (priority queue) which allows any parent node to have 2^x children (where x is a variable of the heap class called spawn_exponent in this implementation)
- The [calculate_child_indices]() and [calculate_parent_index]() util functions use the array indices to find any node's parent or children
- *Insertion*: The insertion property of the heap class uses the [heapify_up]() util to add an element at the end of the heap then 'bubble' it up the heap if its parent or any other ancestor nodes have a lower value
- *pop_max*: To pop off the heap's maximum value and keep it balanced, the [fill_node_holes]() util function goes down the heap picking the maximum value amongst the children nodes to replace a parent node. A "longest ancestry" path is first generated(which is the path from root to "youngest child" element that requires no rebalancing of the heap),and this is used as a guide while going down the heap. When the node being evaluated isn't on this path, a horizontal switch is done, and the [heapify_down]() util function is immediately called to rebalance the heap.


- Reference: [Advanced Data Structures Walmart task on Forage](https://www.theforage.com/virtual-internships/oX6f9BbCL9kJDJzfg?ref=jwa5Z4pAvjDRT4GnD)
- Starting with a Python implementation. Will eventually rewrite in Java.
