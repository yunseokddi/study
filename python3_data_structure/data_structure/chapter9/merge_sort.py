def merge_sort(seq):
    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1:
        left = merge_sort(left)

    if len(right) > 1:
        return merge_sort(right)

    res = []

    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())

    res.reverse()
    return(left or right) + res