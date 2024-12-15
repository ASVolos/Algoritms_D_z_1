# 2*i + 1,  2*i + 2
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        heapify(arr, n, largest)


def heap_sort(any_list):
    n = len(any_list)

    for i in range(n, -1, -1):
        heapify(any_list, n, i)

    for i in range(n - 1, 0, -1):
        temp = any_list[i]
        any_list[i] = any_list[0]
        any_list[0] = temp
        heapify(any_list, i, 0)



my_list = [8, 1, 6, 4, 7, 3, 12, 0, 5, 2, 9, 10, 1, 11, -1]

heap_sort(my_list)
print(my_list)
