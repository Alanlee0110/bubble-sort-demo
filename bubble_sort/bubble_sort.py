"""
Bubble Sort Algorithm

Bubble Sort 是一種簡單的排序演算法,通過多次遍歷數組,
比較相鄰元素並交換順序錯誤的元素,直到數組排序完成。

時間複雜度:
  - 最差/平均/最佳: O(n²)

空間複雜度: O(1)
"""


def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.

    Args:
        arr: List of comparable elements to sort.

    Returns:
        The sorted list (sorted in-place).
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted:", bubble_sort(data))
