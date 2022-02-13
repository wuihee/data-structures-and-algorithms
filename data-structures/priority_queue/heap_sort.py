"""Sort an array of integers via heapsort."""


def heapsort(array):
    """
    Heapsort algorithm.

    Parameters
    ----------
    array : Unsorted array of integers.
    """

    n = len(array)
    build_heap(array)

    # Continuously delete the largest element and store it at the end of the
    # array.
    for i in range(len(array) - 1, -1, -1):
        # Swap the first element (i.e. largest) and the last element of the
        # heap, effectively deleting the largest element.
        array[i], array[0] = array[0], array[i]
        # Reduce array size by 1 after element has been deleted.
        n -= 1
        # Bubble down from the top where new element has just been swapped to
        # maintain the heap invariant.
        heapify(array, n, 0)

    # Return sorted in-place array.
    return array


def build_heap(array):
    """
    Build a max-heap given an unsorted array.

    Parameters
    ----------
    array : Unsorted array of integers.
    """

    n = len(array)
    # Index of last non-leaf node: we do not need to heapify leaves.
    start_idx = n // 2 - 1
    for i in range(start_idx, -1, -1):
        heapify(array, n, i)


def heapify(heap, n, idx):
    """
    Heapify at bubbles down element at idx to maintain heap invariant.

    Parameters
    ----------
    heap : Heap which may have element at idx out of place.
    n : Size of the heap.
    idx : Index position to start bubbling down from.
    """

    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    # Find the position of the largest element between children and parent.
    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right
    
    # If parent (i.e. idx) is not the largest, swap with child
    # # (i.e. bubble down.)
    if idx != largest:
        heap[idx], heap[largest] = heap[largest], heap[idx]
        # Recursively call heapify on the element that was bubbled down until
        # heap invariant is maintained (when children are smaller than parent).
        heapify(heap, n, largest)
