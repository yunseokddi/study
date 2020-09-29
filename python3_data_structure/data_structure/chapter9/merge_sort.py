def merge(left, right):
    if not left or right:
        return left or right

    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())

        else:
            result.append(right.pop())

    result.reverse()
    return (left or right) + result

l1 = [1,2,3,4,5,6,7]
l2 = [2,4,5,8]

print(merge(l1,l2))

