def find_any_peak_1d(a):
    if len(a) <= 2:
        return max(a)
    start = len(a) // 2
    if a[start] < a[start - 1]:
        return find_any_peak_1d(a[:start])
    elif a[start] < a[start + 1]:
        return find_any_peak_1d(a[start + 1:])
    else:
        return a[start]


def find_any_peak_2d(a):
    if len(a) <= 2:
        return max([max(row) for row in a])
    start_row = len(a) // 2
    start_col = a[start_row].index(max(a[start_row]))
    if a[start_row][start_col] < a[start_row - 1][start_col]:
        return find_any_peak_2d(a[:start_row])
    elif a[start_row][start_col] < a[start_row+1][start_col]:
        return find_any_peak_2d(a[start_row+1:])
    else:
        return a[start_row][start_col]
