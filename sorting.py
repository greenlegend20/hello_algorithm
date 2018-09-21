def bubble_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if (ascending and a[j] > a[j + 1]) or (not ascending and a[j] < a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def merge_sort(a, ascending=True, inplace=True):
    if len(a) <= 1:
        return a
    middle = len(a) // 2
    left_list = a[:middle]
    right_list = a[middle:]

    left_list = merge_sort(left_list, ascending=ascending)
    right_list = merge_sort(right_list, ascending=ascending)

    result = []
    while len(left_list) > 0 and len(right_list) > 0:
        if (ascending and left_list[0] < right_list[0]) or (not ascending and left_list[0] > right_list[0]):
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))
    if len(left_list) == 0:
        result += right_list
    else:
        result += left_list
    if inplace:
        for i in range(len(a)):
            a[i] = result[i]
    return result


def insertion_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    for i in range(1, len(a)):
        j = i - 1
        next_element = a[i]
        while ((ascending and a[j] > next_element) or (not ascending and a[j] < next_element)) and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = next_element
    return a


def selection_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    for i in range(len(a)):
        m_i = i
        for j in range(i+1, len(a)):
            if (ascending and a[m_i] > a[j]) or (not ascending and a[m_i] < a[j]):
                m_i = j
        a[i], a[m_i] = a[m_i], a[i]
    return a


def heap_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    def heapify(h, i, end): # stop at end (exclusive)
        l = 2 * i + 1
        r = 2 * i + 2
        m = i
        if l < end and ((ascending and h[i] < h[l]) or (not ascending and h[i] > h[l])):
            m = l
        if r < end and ((ascending and h[m] < h[r]) or (not ascending and h[m] > h[r])):
            m = r
        if m != i:
            h[i], h[m] = h[m], h[i]
            heapify(h, m, end)

    start = len(a) // 2 - 1
    for i in range(start, -1, -1): # build heap
        heapify(a, i, len(a))
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)
    return a


def counting_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    assert min(a) >= 0
    assert max(a) <= 1000000
    count = [0] * (max(a) + 1)
    for i in a:
        count[i] += 1
    i = 0
    for j in (range(len(count)) if ascending else reversed(range(len(count)))):
        for c in range(count[j]):
            a[i] = j
            i += 1
    return a


def radix_sort(a, ascending=True, inplace=True):
    if not inplace:
        a = a[:]
    def get_digit(n, d):
        for i in range(d-1):
            n //= 10
        return n % 10
    def get_num_digit(n):
        i = 0
        while n > 0:
            n //= 10
            i += 1
        return i

    m = max(a)
    assert min(a) >= 0
    assert m <= 1000000
    for d in range(1, get_num_digit(m)+1):
        count = [[] for _ in range(10)]
        for num in a:
            count[get_digit(num, d)].append(num)
        i = 0
        for j in (range(10) if ascending else reversed(range(10))):
            for num in count[j]:
                a[i] = num
                i += 1
    return a