def solution(A):
    """
    Computes inversions in A, returns -1 if len(A) > 1,000,000,000.
    """
    if len(A) > 1_000_000_000:
        return -1
    return count_inversions(A, 0, len(A) - 1)


def count_inversions(A, left, right):
    """
    Recursively counts inversions in A[left:right+1].
    """
    if left >= right:
        return 0

    mid = (left + right) // 2
    left_inversions = count_inversions(A, left, mid)
    right_inversions = count_inversions(A, mid + 1, right)
    merged_inversions = merge_and_count(A, left, mid, right)

    return left_inversions + right_inversions + merged_inversions


def merge_and_count(A, left, mid, right):
    """
    Merges subarrays, counts inversions between them.
    """
    i = left
    j = mid + 1
    merged = []
    inversions = 0

    while i <= mid and j <= right:
        if A[i] > A[j]:
            merged.append(A[j])
            inversions += mid - i + 1
            j += 1
        else:
            merged.append(A[i])
            i += 1

    while i <= mid:
        merged.append(A[i])
        i += 1

    while j <= right:
        merged.append(A[j])
        j += 1

    for i in range(left, right + 1):
        A[i] = merged[i - left]

    return inversions