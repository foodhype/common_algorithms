def kadanes(a):
    """maximum contiguous sum"""
    max_here = 0
    max_sum = 0
    for i in a:
        max_here = max(0, max_here + i)
        max_sum = max(max_sum, max_here)
    return max_sum
