def bubble_sort(a, ascending=True):
    result = a.copy()
    for i in range(len(result) - 1, 0, -1):
        for j in range(i):
            if (ascending and result[j] > result[j + 1]) or (not ascending and result[j] < result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def merge_sort(a, ascending=True):
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
    return result


def insertion_sort(a, ascending=True):
    result = a.copy()
    for i in range(1, len(result)):
        j = i - 1
        next_element = result[i]
        while ((ascending and result[j] > next_element) or (not ascending and result[j] < next_element)) and j >= 0:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = next_element
    return result


def selection_sort(a, ascending=True):
    result = a.copy()
    for i in range(len(result)):
        m_i = i
        for j in range(i+1, len(result)):
            if (ascending and result[m_i] > result[j]) or (not ascending and result[m_i] < result[j]):
                m_i = j
        result[i], result[m_i] = result[m_i], result[i]
    return result
