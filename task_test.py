
def solution(A):
    # remove negatives and zeros
    A = [number for number in A if number > 0]
    if not A:
        return 1

    A.sort()
    sorted_ids = A
    a = sorted_ids[0]
    b = sorted_ids[-1]
    unique_sorted_ids = list(set(sorted_ids))

    if unique_sorted_ids[0] is not 1:
        return 1

    for number in range(a, b, 1):
        if number not in sorted_ids:
            return number

    return sorted_ids[-1] + 1


if __name__ == '__main__':
    # A = [1, 3, 6, 4, 1, 2]
    # A = [1, 2, 3]
    # A = [-1, -3]
    A = [2, 2, 8]
    print(solution(A))
