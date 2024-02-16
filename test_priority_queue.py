#%%
import priority_queue


def test_get_parent():
    pq = [2,6,3,10,12,5]
    assert priority_queue.get_parent(pq, 0) is None
    assert priority_queue.get_parent(pq, 5) == 2
    assert priority_queue.get_parent(pq, 4) == 1


def test_get_childs():
    pq = [2,6,3,10,12,5]
    assert priority_queue.get_right_child(pq, 2) is None
    assert priority_queue.get_right_child(pq, 0) == 2
    assert priority_queue.get_right_child(pq, 5) is None

    assert priority_queue.get_left_child(pq, 0) == 1
    assert priority_queue.get_left_child(pq, 2) == 5
    assert priority_queue.get_left_child(pq, 5) is None


def test_compare():
    pq = [2,6,3,10,12,5]
    assert priority_queue.compare(pq[0], pq[3]) == True
    assert priority_queue.compare(None, pq[0]) == False
    assert priority_queue.compare(pq[0], None) == False


def test_get_smallest_child():
    pq = [2,6,3,10,12,5]
    priority_queue.get_smallest_child(pq, 0) == 2
    priority_queue.get_smallest_child(pq, 2) == 5
    priority_queue.get_smallest_child(pq, 1) == 3
    priority_queue.get_smallest_child(pq, 5) is None


def test_top():
    pq = [2,6,3,10,12,5]
    assert priority_queue.top(pq) == 2
    assert pq == [2,6,3,10,12,5]


def test_swap():
    pq = [2,6,3,10,12,5]
    priority_queue.swap(pq, 0, -1)
    assert pq == [5,6,3,10,12,2]


def test_insert():
    pq = [2,6,3,10,12,5]
    priority_queue.insert(pq, 1)
    assert pq == [1,6,2,10,12,5,3]


def test_pop():
    pq = [2,6,3,10,12,5]
    v = priority_queue.pop(pq)
    assert v == 2
    assert pq == [3,6,5,10,12]

    pq = [2,3,10]
    v = priority_queue.pop(pq)
    assert v == 2
    assert pq == [3,10]


def test_from_list():
    lst = [10, 3, 5, 6, 12, 2]
    pq = priority_queue.from_list(lst)
    assert pq == [2,6,3,10,12,5]



# %%
