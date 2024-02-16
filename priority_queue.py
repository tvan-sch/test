def get_parent(pq, index):
    """ returns the index of the parent or none if already at the root """
    pass


# To test the following two functions run test_get_childs()
def get_left_child(pq, index):
    """returns index of the left child if it exists, else none"""
    pass


def get_right_child(pq, index):
    """returns index of the right child if it exists, else none"""


def compare(v1, v2, comparator=lambda x,y: x < y) -> bool:
    """ Lambda is a concept with which we can bind a function to a variable. X and Y are the parameters of the function.
    So comparator(x,y) returns True if x is smaller than y, and False if x is not smaller than y.
    Replace x and y with the correct variable names. Peek at the test functions for more hints."""
    pass


def get_smallest_child(pq, index):
    """ return the smallest child, check the test function to find out what to do when one of the children doesn't exist"""
    pass


def top(pq):
    """ return the index of the top of the priority queue"""
    pass


def swap(pq, i, j):
    """ swap two elements in the priority queue"""
    pass


def insert(pq, value):
    """ Add the value at the end of the priority queue and keep swapping until the invariant is preserved again """
    pass


def pop(pq):
    """ Remove the top element and then reorder the priority queue so that the shape and invariant are preserved again.
    Finally, return the removed top element. """
    pass


def from_list(lst):
    """ Convert a list into a priority queue, only use functions insert, top or pop"""
    pass

